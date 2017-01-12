# Add New Commands

In order to add new commands go into the `commands` folder and create the following structure:
```
commands/
 └─── new_command/
      |- __init__.py
      │- new_command.py
```
- Create a new folder with the command name for simplicity
- Add an empty `__init__.py` file
- Add a new python file with the command name (again for simplicity reasons) where you'll add your code
- Inside main_commands.py import the functionality created and edit the function `process_command` in order to call your functionality
- Add the command to the bot configuration file in `bot_config.json`. Format:
```
"command": {
  "triggers": [
    "words",
    "that",
    "will",
    "trigger",
    "this",
    "command"
  ]
}
```
  - **triggers:** the words that will trigger the added command

- The new command implementation **must** return a `flag (boolean)` and a `result (string)` in this order:
  - **flag (boolean)** - if it's true the bot will say the result, otherwise the result will be presented without any voice feedback.
  - **result (string)** - the text that will be returned and sayid by the bot of the previous is true;

- Check the `ping` command for an simple example.
