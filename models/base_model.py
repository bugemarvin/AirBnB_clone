#!/usr/bin/python3
from uuid import uuid
from datetime import datetime
'''
contians all defined attributes/methods for other classes.
'''

class BaseModel:
    def __init__(*arg, **kwargs):
        self.id = str(uuid.uui4())
	if isinstance(Basemode, self.id) == True:
            self.created_at = datetime.now()
            if created_at in BaseModel not None:
                self.updated_at = datetime.now()
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
