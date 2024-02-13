#!/usr/bin/python3
"""amenity model"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class for place class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """constructor for Amenity class

        arguments:
        name : str for amenity name
        """

        super().__init__(*args, **kwargs)
