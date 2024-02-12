#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel as Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = FileStorage.__objects
        serialized_objects = {key: obj.to_dict() for key, obj in objects_dict.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objects_dict = json.load(file)
                for obj_id, obj_data in objects_dict.items():
                    class_name = obj_data.pop("__class__")
                    cls = eval(class_name)
                    obj_instance = cls(**obj_data)
                    FileStorage.__objects[obj_id] = obj_instance
        except FileNotFoundError:
            return

