from ping.ping import pong
from ifttt.ifttt import ifttt_call
from wolfram_question.question import Question as Q
from translate.translate import translate
from traffic.traffic import Traffic as T


question = Q()
traffic = T()


def process_command(command, message=""):
    """Returns a flag (boolean) and the result of executing the command, usually a string for the to say.
    Set the talk flag to true if you want the bot to speak otherwise set it to false.
    Will also return a voice setting for translations.    
    
    Keyword arguments:
    command -- the command received
    message -- the message received, empty by default
    """

    talk = True
    _voice = None
    result = "Sorry but that command is not part of my functions."

    if command == "ping":
        talk, result = pong()
    elif command == "play song on android":
        talk, result = ifttt_call("play_song_on_android", {"value1" : "Alan Walker - Faded", "value2" : "", "value3" : ""})
    elif command == "question":
        talk, result = question.get_question_result(message)
    elif command == "translate":
        talk, result, _voice = translate(message)
    elif command == "traffic":
        talk, result = traffic.traffic(message)

    return talk, result, _voice
