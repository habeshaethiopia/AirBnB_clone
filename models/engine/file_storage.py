#!/usr/bin/python3
"""the persstant storage"""
import json

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

class FileStorage:
    """the file storage class"""
    clss = {
            "User": User,
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
            }
    __file_path = "models/engine/file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of object"""
        return FileStorage.__objects

    def new(self, obj):
        """create anew object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """to json and save it to file"""
        saved_dict = {}
        for key, obj in FileStorage.__objects.items():
            saved_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(saved_dict))

    def reload(self):
        deseri = {}
        """To relode from the json file"""
        try:
            with open(self.__file_path) as file:
                deseri = json.loads(file.read())
            for key, value in deseri.items():
                FileStorage.__objects[key] = FileStorage.clss[key.split('.')[
                    0]](**value)
        except FileNotFoundError:
            pass
