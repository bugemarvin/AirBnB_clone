#!/usr/bin/python3
from uuid import uuid4 UUID
from datetime import datetime
'''
contians all defined attributes/methods for other classes.
'''

class BaseModel:
    '''
    creating class variables for the base model.
    '''
    base_date = datetime.now()
    def __init__(*arg, **kwargs):
	'''
        Declaring public instance attribute for id.
        '''
        self.id = str(uuid.uui4())
        self.created_at = self.base_date
        self.updated_at = self.base_date
    '''
    Using Dunder method __str__() for out put.
    '''
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    '''For Debuging incase __str__() fails'''
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
