# AirBnB_clone

## Description
The goal of the AirBnB clone project is to deploy a simple copy of the AirBnB website on our own servers
After 4 months the goal is to  have a complete web application composed by:
+ A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
+ A website (the front-end) that shows the final product to everybody: static and dynamic
+ A database or files that store data (data = objects)
+ An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them

The first step is to write a command interpreter to manage the AirBnB objects.

## Command Interpreter
The command interpreter is used to manage the objects of our project:
+ Create a new object (ex: a new User or a new Place)
+ Retrieve an object from a file, a database etc
+ Perform operations on objects (count, compute stats, etc)
+ Update attributes of an object
+ Destroy an object


## Execution
The shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Requirements

### Python Scripts
+ All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
+ All modules, classes and functions should have a documentation
+ A README.md file, at the root of the folder of the project

### Python Unit Tests
+ All test files should be inside a folder test
+ The unittest module must be used
+ The file organization in the tests folder should be the same as in the project
+ All test files and folders should start by `test_`
+ All tests should be executed by using this command:`python3 -m unittest discover tests`
+ The unittest module must be used 


## Files and Directories

| File | Description |
|---------- | ---------- |
| console.py | Contains the entry point of the command interpreter |
| models/base_model.py | Defines all common attributes/methods for other classes |
| models/engine | |
| models/user.py| Contains class user that inherites from BaseModel|
| models/engine/file_storage.py | serializes instances to a JSON file and deserializes JSON file to instances |
| models/state.py | Contains class `User` that inherites from  `BaseModel` |
| models/city.py | Contains class `City` that inherites from  `BaseModel` |
| models/amenity.py |  Contains class `Amenity` that inherites from  `BaseModel` |
| models/place.py | Contains class `Place` that inherites from `BaseModel` |
| models/review.py |  Contains class `Review` that inherites from  `BaseModel` |



