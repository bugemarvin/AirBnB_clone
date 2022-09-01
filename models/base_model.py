#!/usr/bin/python3
import uuid
from datetime import datetime
'''
class BaseModel that defines all common attributes/methods for other classes.
'''

class BaseModel:
    '''
    id: string - assign with an uuid when an instance is created:
        you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
        the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance is created
    updated_at: datetime - assign with the current datetime when an instance is created 
                and it will be updated every time you change your object
    '''
    id = None
    created_at = None
    updated_at = None
    def __init__(self, *args, **kwargs):
        '''
        you will use *args, **kwargs arguments for the constructor of a BaseModel. 
	                                 (more information inside the AirBnB clone concept page)
        *args won’t be used
        if kwargs is not empty:
                            each key of this dictionary is an attribute name 
                                  (Note __class__ from kwargs is the only one that should not be 
                                         added as an attribute. See the example output, below)
                            each value of this dictionary is the value of this attribute name
        Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance
                 is working with datetime object. You have to convert these strings into datetime object.
        '''
        if kwargs:
            for key,value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        if not BaseModel.id:
            self.id = str(uuid.uuid4())
        if not BaseModel.created_at:
            self.created_at = self.updated_at = datetime.now()
        if not BaseModel.updated_at:
            self.updated_at = datetime.now()
    '''
    Using Dunder method __str__() for out put.
    '''
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    '''
    For Debuging incase __str__() fails
    '''
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
        pass
    
    '''
    create format of output for the dunder __dict__ of an instance created.
    '''
    def to_dict(self):
        pass
