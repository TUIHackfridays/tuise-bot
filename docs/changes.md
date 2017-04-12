# Changes
Added an AI Puzzle Solver to the bot.

The puzzle solver works by uing the [A* algorithm](http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html). An algorithm that will find, if possible, the optimal solution to solve the puzzle.

Adding the following new endpoints:
- **[GET] puzzle** -- get a random puzzle **[Warning]** may not be a solvable puzzle
- **[POST] puzzle** -- get step by step solution for the puzzle if exists

## New dependencies
No new dependencies.

## New triggers
```
"triggers": [
  "solve a puzzle",
  "puzzle solver",
  "puzzle"
]
```

## Changes (03-03-2017)
The configurations files were moved inside a config folder to keep things more organized if your `config.cfg` in the project root move it inside the `config` folder.

New endpoints where created to interact with the database data.
- **[GET] translation-locales** -- get the locales that the bot can speak for translations
- **[GET] bot-settings-all** -- get all the bot settings
- **[GET|POST] bot-settings** -- get and set the bot settings

### New dependencies
- For Database:
  * sqlite
- For traffic:
  * lxml
  * geopy

### sqlite
- Install sqlite:
  * For Windows and Mac OS go to [sqlite website](http://sqlitebrowser.org/), download and install it.
  * For Linux run the command `sudo apt-get install sqlite3`

#### Note
Python should have sqlite3 module in the standard library but in case it's missing run `$VENV/bin/pip install pysqlite`

You can also use sqlitebrowser to see and query the database. Just open the `tuise_database.db` file located on the `db` folder.

[<< back](./README.md)
