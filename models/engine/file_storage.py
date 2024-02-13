#!usr/bin/python3
""" File storage model """
import json


class FileStorage():
    """
    FileStorage class for file operations
    """

    __file_path = "file.json"
    __objs = {}

    def all(self):
        """
        Returns all objects
        """
        return self.__objs

    def model_classes(self):
        """Returns classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        models = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
                   }
        return models

    def new(self, obj):
        """
        Add obj to objects
        """
        self.__objs[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """"
        Serialize __objs to json objects for save it
        """
        serialize_objects = {}
        for key, value in self.__objs.items():
            serialize_objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as json_file:
            json.dump(serialize_objects, json_file, indent=4)

    def reload(self):
        """
        Deserializes the JSON
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as json_file:
                serialize_objects = json.load(json_file)

            for key, value in serialize_objects.items():
                contor = value["__class__"]
                if contor in self.model_classes.keys():
                    self.__objs[key] = self.model_classes[value["__class__"]](
                        **value)
        except FileNotFoundError:
            pass
        except Exception as error:
            pass
