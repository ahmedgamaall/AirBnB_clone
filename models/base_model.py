#!/usr/bin/python3
"""this is the base model for all classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class that all classes inherit from"""
    
    def __init__(self):
        """Instance Constructor.

        arguments:
        id:unique identifier
        created_at: created date
        updated_at: updated date
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """__str__

        Returns: string
        """
        print(f"[<class name>] (<self.id>) <self.__dict__>")

    def save(self):
        """save

        update the updated_at argument
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """To_dict
        
        corvet data to json

        Returns:
            dict: dictionary representation.
        """
        my_class_dict = self.__dict__.copy()
        my_class_dict["__class__"] = self.__class__.__name__
        my_class_dict["updated_at"] = self.updated_at.isoformat()
        my_class_dict["created_at"] = self.created_at.isoformat()
        return my_class_dict

