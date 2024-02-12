#!/usr/bin/python3
"""review model"""
from models.base_model import BaseModel

class Review(BaseModel):
    """review class for place class"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor for Review class

        arguments:
        place_id : str for review place id
        user_id : str for review user id
        text : str for review text
        """

        super().__init__(*args, **kwargs)