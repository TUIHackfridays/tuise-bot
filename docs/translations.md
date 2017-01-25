# Using the translations

## Calling the command
To use this command call the bot and then say **"translate [sentance to translate] to [language to translate it to]"**. Example: `translate hello how are you to portuguese`.

## Supportes languages

In order for the bot to speak the translations only some languages are supported.

Here's the list:

* Danish
* Dutch
* English
* French
* German
* Icelandic
* Italian
* Norwegian
* Polish
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkish
* Welsh

## Implemetation

The code in `translate.py` has the following functions:
- `translate` - will check if the desired language is supported and return the translation and the voice configurations to speak in the language or `None` if not supported
- `_get_valid_locale` - will get the list of supported languages and check if the desired one is supported returning the locale or `Ǹone` if not supported
- `_caseless_equal` - will validate if the inputed pattern is in the inputed text returning `True` or `False`
- `_get_parameters` - will parse the recieved input to get the the sentece and the desired language to translate

## Note
This functionality uses Google to get the translations but the voices the bot can speak in are limited. If you want you can reuse this and make a text only return version like discribed bellow.

### Text only translations
In order to support more languages you'll need to change the `_get_valid_locale` and `translate` functions.

#### Changes in `_get_valid_locale`
- Replace the configuration file to `supported_translation_locale.json`
- Update the loop to get the language and locale from the new file
- Remove the voice and return the locale only
- Update the `_get_parameters` function to get the proper return from the `_get_valid_locale` function

#### Changes in `translate`
- Remove the voice and return the locale only
- Return `False` insted of `True` as the first parameter as we don't want the bot the speak the result
