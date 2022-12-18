
# Version History Changelog
## Project 4
1. Added "ClientWorker" class: A thread that is started up by the Model.
Thread initially sleeps and is woken up by the "request_data" method to retrieve the needed data. Then sends a signal back to the GUI event loop with the data.
    - Updated the UML model with this class


## Project 3
1. ./src/system.py was replaced by ./src/main.py: Console-based application has been erased at commit: 4676e2a2bb3c115a9b5de5f96946c9c1d4a8ff77

Most printing methods have been left in various classes just for unit testing

2. Developed GUI components found in ./src/gui
    -Models Contain data oriented GUI elements' models
    -Views contain the generated view definitions and their asscoieted controller.

Server data now shows on the GUI in a table based view. Does not effectively check connection to internet. Choosing to wait for project 4's requirement on multithreading to handle that since it would probably change the interface significantly, and there is no real gain right now.

Most Recent First
## Project 2

1. Communicate with sports.snoozle.net servers REST API
2. Support printing a JSON object in a user-friendly manner to the console or a file with
printing of team name, team number and season record.
3. Store JSON response data object.

- Added "online" package
- Renamed "json_49ers_serdes" to "nfl_json_serdes"
- Implmeneted new front-end features in run.py that contribute to project 2 feature goals
    - An option to load statistics from sports.snoozle.net into memory and manipulate the list using the existing features
    - An option to print out a simple one liner for a given team's W/L record




## Project 1
1. Supports parsing a given json file or a json string and transform them into an object representation.
2. Supports printing a JSON object in a user-friendly manner to the console or a file.
3. Supports support generating a new JSON object and adding to an existing object to create a more
complex object hierarchy.
4. Support querying a given JSON object to retrieve the value associated with the query
string.