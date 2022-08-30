#!/usr/bin/python3
'''
contians all defined attributes/methods for other classes.
'''

class BaseModel:
    def __init__(self, id):
        id = uuid.uuid4()
        self.id = id
