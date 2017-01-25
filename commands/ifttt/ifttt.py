from ConfigParser import RawConfigParser
from requests import post

def ifttt_call(event, payload=None):
    # get configuration
    configParser = RawConfigParser()
    configFilePath = r'config/config.cfg'
    configParser.read(configFilePath)
    ifttt_key = configParser.get('main', 'ifttt_key')
    request_url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, ifttt_key)

    if payload is not None:
        r = post(request_url, data=payload)
    else:
        r = post(request_url)

    if r.status_code == 200:
        return False, r.text
    else:
        return False, "Something went wrong. %s" % r.text
