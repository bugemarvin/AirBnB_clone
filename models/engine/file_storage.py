#!/usr/bin/python3
"""A module that serializes instances to a
JSON file and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that stores objects in JSON format

    Attributes:
        __file_path(str): path to the JSON file
        __objects(dict): empty dict to store all objects by <class name>.id


    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (if JSON
        file exists else do nothing)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            new = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new, f)

    def reload(self):
        """
        deserializes the JSON file to __objects if Json file exists
        else do nothing.
        if the file doesn’t exist, no exception should be raised
        """
        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                'City': City, 'Amenity': Amenity, 'Place': Place,
                'Review': Review}

        try:
            dic = {}
            with open(FileStorage.__file_path, 'r') as f:
                dic = json.load(f)
                for k, v in dic.items():
                    self.all()[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass
