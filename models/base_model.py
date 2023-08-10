#!/usr/bin/python3
"""this is the base class module"""
import uuid
from datetime import datetime


class BaseModel:
    """class base"""

    def __init__(self, *args, **kwargs):
        """class instantiontion"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """the string representation"""
        return ("[{}] ({}) {}".format(str(self.__class__.__name__), str(self.id), str(self.__dict__)))

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary"""
        Dict = {}
        for a, b in self.__dict__.items():
            if a == 'created_at':
                b = self.created_at.isoformat()
            if a == 'updated_at':
                b = self.updated_at.isoformat()
            Dict[a] = str(b)
        Dict["__class__"] = str(self.__class__.__name__)
        return Dict
