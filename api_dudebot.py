import logging
import pyvona
import ConfigParser
import random
import json
import socketio
import eventlet

from socketio import Middleware
from eventlet import wsgi

from pyramid.config import Configurator
from pyramid.view import view_config

from commands.main_commands import process_command


# setup logging
logging.basicConfig(filename='dudebot.log', level=logging.DEBUG)
log = logging.getLogger(__file__)

# get configuration
configParser = ConfigParser.RawConfigParser()
configFilePath = r'config/config.cfg'
configParser.read(configFilePath)

access_key = configParser.get('main', 'access_key')
secret_key = configParser.get('main', 'secret_key')

# bot triggers default
triggers = ['hey dude']

# available commands
commands = { "question" : ['question', 'questions', 'pergunta', 'questao']}

# greetings default
greetings = ["Yes?"]

# setup pyvona voice
voice = pyvona.create_voice(access_key, secret_key)
voice.voice_name="Brian"
voice.language="en-GB"
voice.gender="Male"

translation_voice = None

# socket io
sio = socketio.Server()
socketID = None

# app setup
port = 8080


def load_bot_configuration():
    with open('config/bot_config.json') as json_data:
        bot_conf = json.load(json_data)

    return bot_conf


def callBotAnimation(started):
    if socketID is not None:
        sio.emit('speak', data={"started": started}, room=socketID)


def speak(text):
    global translation_voice
    log.info("text to speak - %s" % text)

    if translation_voice is not None:
        voice.voice_name = translation_voice["voice_name"]
        voice.language = translation_voice["language"]
        voice.gender = translation_voice["gender"]
    else:
        voice_cnf = load_bot_configuration()["voice"]
        voice.voice_name = voice_cnf["voice_name"]
        voice.language = voice_cnf["language"]
        voice.gender = voice_cnf["gender"]

    voice.speak(text)
    callBotAnimation(False)
    translation_voice = None


def threadSpeak(text):
    callBotAnimation(True)
    eventlet.spawn(speak, text=text)


# views
@view_config(
    route_name='ping',
    request_method=('GET'),
    renderer='json'
)
def ping(request):
    request.response.status = 200
    log.info(voice.list_voices())
    return {"message": "pong"}


@view_config(
    route_name='trigger',
    request_method=('GET'),
    renderer='json'
)
def listen(request):
    greetings = load_bot_configuration()["greetings"]
    greet = random.choice(greetings)
    log.info(greet)
    threadSpeak(greet)
    request.response.status = 200
    return {"message": greet}


@view_config(
    route_name='triggers',
    request_method=('GET'),
    renderer='json'
)
def get_triggers(request):
    triggers = load_bot_configuration()["triggers"]
    request.response.status = 200
    return {"triggers": triggers}


@view_config(
    route_name='commands',
    request_method=('GET'),
    renderer='json'
)
def get_commands(request):
    commands = load_bot_configuration()["commands"]
    request.response.status = 200
    return commands


@view_config(
    route_name='execute',
    request_method=('POST'),
    renderer='json'
)
def execute_command(request):
    global translation_voice
    
    data = request.json_body
    log.info(data)
    talk = True
    result = "Sorry but I cannot recognize the command."
    if data["command"]:
        talk, result, translation_voice = process_command(data["command"], data["content"])

    if talk:
        threadSpeak(result)

    request.response.status = 200
    return {"message": result}


@view_config(
    context='pyramid.exceptions.NotFound',
    renderer='json'
)
def notfound_view(request):
    request.response.status = '404 Not Found'
    return { "code" : 404, "message" : 'Not Found'}


# -------------------- Socket io ------------------


@sio.on('connect')
def connect(sid, environ):
    global socketID
    socketID = sid
    log.info('connect %s' % sid)
    sio.emit('connect', data={"user connected": socketID}, room=socketID)
    

@sio.on('disconnect')
def disconnect(sid):
    global socketID
    socketID = None
    log.info('disconnect %s' % sid)
    sio.emit('disconnect', data={"user disconnected": sid})


if __name__ == '__main__':
    log.info("App listening at port %d" % port)
    # configurations settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all']  = True
    # configuration setup
    config = Configurator(settings=settings)
    # routes setup
    config.add_route('ping', '/ping')
    config.add_route('triggers', '/available-triggers')
    config.add_route('trigger', '/trigger')
    config.add_route('commands', '/commands')
    config.add_route('execute', '/execute')
    config.add_static_view('/', 'site', cache_max_age=3600)
    # scan for @view_config decorators
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    # wrap application with socketio's middleware
    app_wrap = Middleware(sio, app)
    wsgi.server(eventlet.listen(('0.0.0.0', port)), app_wrap)