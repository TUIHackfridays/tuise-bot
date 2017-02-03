# Traffic

## Calling the command
To use this command call the bot and then say **"traffic information"** or **"traffic in [the location]"**. Example: `traffic in Amsterdam Netherlands`.

## Implementation

The code in `traffic.py` has the following functions:
- `traffic` - will return the traffic information found for that location or if the location is `None` will get the information disregarding the location information
- `_get_parameters` - will parse the recieved input to get the location

## Note

This functionality uses the implemented `ndw` class that does the fetching, parsing and gets the traffic information but since this needs to get the locations based on the coordinates it takes a lot of time to get a response.
