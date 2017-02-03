import json
import re

from urllib import quote
from requests import get


def translate(message):
    """
    Translate the source_text parameter from english into the 
    target_lang if possible to speak.
    Returns by order:
    the speak flag as True if we want the bot to speak, False if we don't
    the text to speak
    the voice configuration if there's any or else it's None
    
    Keyword arguments:
    message -- the full command with the sentece to translate.
    """
    
    voice, target_lang, source_text = _get_parameters(message)
    
    if target_lang is not None:
    
        source_lang = "en-US"
        
        url = "https://translate.googleapis.com/translate_a/single?" + \
        "client=gtx&sl=" + source_lang + "&tl=" + target_lang + \
        "&dt=t&q=" + quote(source_text)
        
        r = get(url)
        
        if r.status_code == 200:
            pattern = re.compile('\"(.*?)\"', re.IGNORECASE)
            matches = pattern.search(r.text)
            if matches is not None:
                res = matches.group(0)
                if res is not None and len(res) > 0:
                    return True, res, voice 
    
        return True, "Sorry, something went wrong and I could not do the translation.", voice
        
    return True, "Sorry, but I still don't know how to speak in that language.", None


def _get_valid_locale(language):
    """
    Get a valid location and the voice configuration fot that language 
    for the translation.
    
    Keyword arguments:
    language -- the language for the translation
    """
    with open('config/supported_translation_voices.json') as json_data:
        voices = json.load(json_data)

    selected_voice = None
    locale = None
    
    for index, voice_lang in enumerate(d['voice_language'] for d in voices): 
        if _caseless_equal(language, voice_lang):
            selected_voice = voices[index]
            locale = voices[index]['language']
            break
    
    return selected_voice, locale


def _caseless_equal(text, pattern):
    """
    Returns the comparison between the two inputed words 
    (case insensitive) by checking if the text contains the pattern.
    
    Keyword arguments:
    text -- the text to check for the pattern on
    pattern -- the pattern to search in the text
    """
    return re.search(pattern, text, re.IGNORECASE) is not None


def _get_parameters(message):
    """Get the source_text and target_lang parameters
    from the user input.
    
    Keyword arguments:
    message -- the full command with the sentece to translate.
    """
    # clean translate command
    text_input = message[0].lower().replace("translate", "", 1)
    to_index = text_input.rfind("to")
    voice, target_lang = _get_valid_locale(text_input[to_index + 2:].strip())
    source_text = text_input[:to_index].strip()
    
    return voice, target_lang, source_text