#!/usr/bin/python3
from uuid import uuid
from datetime import datetime
'''
contians all defined attributes/methods for other classes.
'''

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uui4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
