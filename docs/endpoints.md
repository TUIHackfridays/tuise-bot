# BOT API Endpoints

# GET /ping
Get server `pong` response
+ Response 200 (application/json)
    + Attributes (object)
        - message: pong (string)
    + Body

        ```json
        {"message": "pong"}
        ```

# GET /trigger
Trigger bot to speak one of the greetings
+ Response 200 (application/json)
    + Attributes (object)
        - message: bot response (string)
    + Body

        ```json
        {"message": "bot response"}
        ```

# GET /available-triggers
Get the triggers words that should trigger the bot greetings responses
+ Response 200 (application/json)
    + Attributes (object)
        - triggers:["word1", "word2", "word3"]\(array of strings)
    + Body

        ```json
        {"triggers": ["word1", "word2", "word3"]}
        ```

# GET /commands
Get the commands and commands configuration
+ Response 200 (application/json)
    + Attributes (object)
        - command: (object) the defined command
          - triggers: ["command-trigger-word1", "command-trigger-word2", "command-trigger-word3"]\(array of strings)
    + Body

        ```json
        {
          "command": {
            "triggers": [
              "command-trigger-word1",
              "command-trigger-word2",
              "command-trigger-word3"
            ]
          }
        }
        ```

# POST /execute
Tell the bot to execute the command
+ Request (application/json)
    + Attributes (object)
        - command: command (string)
        - content: ["stt-result-1", "stt-result-2", "stt-result-3", ...]\(array of strings)
    + Body

        ```json
      {
        "command": "ping",
        "content": ["ping", "bing"]
      }
      ```

+ Response 200 (application/json)
    + Attributes (object)
        - message: command result (string)
    + Body

        ```json
        {"message": "command result"}
        ```

# GET /translation-locales
Get the list of available languages/locales that the bot can speak in do the translations.
+ Response 200 (application/json)
    + Attributes (object)
        - message: ["locale-1", "locale-2", "locale-3", ...]\(array of strings)
    + Body

        ```json
        {"message": ["Danish", "Dutch", "English"]}
        ```

# GET /bot-settings-all
Get the list of the voices settings that the bot can speak in.
+ Response 200 (application/json)
    + Attributes (object)
        - message: [{settings object-1}, {settings object-2}, {settings object-3}, ...]\(array of objects)
    + Body

        ```json
        {"message": [
          {"language": "en-US", "id": 1, "voice_name": "Salli", "gender": "Female"},
          {"language": "en-US", "id": 2, "voice_name": "Joey", "gender": "Male"},
          {"language": "da-DK", "id": 3, "voice_name": "Naja", "gender": "Female"},
          {"language": "da-DK", "id": 4, "voice_name": "Mads", "gender": "Male"}]
        }
        ```

# GET /bot-settings
Get the current bot voice settings.
+ Response 200 (application/json)
    + Attributes (object)
        - message: {settings object} (object)
    + Body

        ```json
        {"message": {"language": "en-GB", "id": 10, "voice_name": "Brian", "gender": "Male"}}
        ```

# POST /bot-settings
Set the current bot voice settings, it should be one of the ids of the endpoint `GET /bot-settings-all`.
+ Request (application/json)
    + Attributes (object)
        - settings: value (INTEGER)
    + Body

        ```json
      {
        "settings": 10
      }
      ```

+ Response 200 (application/json)
    + Attributes (object)
        - message: message (string)
    + Body

        ```json
        {"message": "New bot settings was set OR New bot settings was not set"}
        ```

[<< back](./README.md)
