#!/usr/bin/python3
"""this is the base model for all classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class that all classes inherit from"""
    my_number = 90

    def __init__(self, *args, **kwargs):
        """constructor for BaseModel class

        arguments:
        id:unique identifier
        created_at: created date
        updated_at: updated date
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    elif key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """__str__

        Returns : string
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save

        update the updated_at argument
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """To_dict

        corvet data to json
        Returns : dict: dictionary
        """
        class_dictionary = self.__dict__.copy()
        class_dictionary["__class__"] = self.__class__.__name__
        class_dictionary["updated_at"] = self.updated_at.isoformat()
        class_dictionary["created_at"] = self.created_at.isoformat()

        return class_dictionary
