#!/usr/bin/python3
"""this is the base class module"""
import uuid
from datetime import datetime


class BaseModel:
    """class base"""

    def __init__(self, *args, **kwargs):
        """class instantiontion"""
        if kwargs is not None and len(kwargs)>0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        val = value
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """the string representation"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

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
            Dict[a] = b
        Dict["__class__"] = self.__class__.__name__
        return Dict
