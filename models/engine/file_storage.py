#!/usr/bin/python3
"""the persstant storage"""
import json


class FileStorage:
    """the file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of object"""
        return self.__objects

    def new(self, obj):
        """create anew object"""
        key = "{}.{}".format(obj.__class__.name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """to json and save it to file"""
        with open (self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))
    def reload(self):
        deseri = {}
        """To relode from the json file"""
        try:
            with open (self.__file_path) as file:
                deseri = json.loads(file.read())
            for key,value in deseri.items():
                self.__objects[key] = value
        except FileNotFoundError:
            pass