#!/usr/bin/python3
"""
Defines the base Class(BaseModel) for the project
"""
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """
    class BaseModel that defines all common attributes/methods
    for other classes

    Attributes:
        id(str): assign with an uuid when an instance is created:
        created_at: assigns the current datetime when an instance is created
        updated_at: assigns the current datetime when an instance is created
                and updates every time  the object is changed

    Methods:
        __str__: returns a string with class name, id and dict object
        to_dict: Returns a dictionary representation of an object
        save: updates the  'update_at' attribute to current time
    """
    cur_date = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Initialization of public attributes

        Args:
            args: arguments
            kwargs: key/value attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = self.cur_date
        if not self.id:
            self.id = str(uuid.uuid4())
        if not self.created_at:
            self.created_at = self.updated_at = self.cur_date
        if not self.updated_at:
            self.updated_at = self.cur_date
        models.storage.new(self)

    def __str__(self):
        """
        returns a string with class name, id and dict object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def __repl__(self):
        '''
        Returns dunder __str__() if it fails.
        '''
        return self.__str__()

    '''
    To update public instance update_at for created already created instance.
    with the current date of the updated obj in it's instance class.
    '''
    def save(self):
        """
        updates the  'update_at' attribute to current time
        """
        self.updated_at = self.cur_date
        models.storage.save()

    '''
    create format of output for the dunder __dict__ of an instance created.
    '''
    def to_dict(self):
        """Returns a dictionary representation of an object
        """
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = str(type(self).__name__)
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
