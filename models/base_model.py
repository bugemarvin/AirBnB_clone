#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
'''
contians all defined attributes/methods for other classes.
'''

class BaseModel:
    def __init__(self, id, date):
        self.id = uuid.uui4()
        self.date = datetime.now()
    def created_at(self):
        return self.date
    def updated_at(self, updated_date):
        self.date = updated_date
