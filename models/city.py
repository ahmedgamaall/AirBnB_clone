#!/usr/bin/python3
"""city model"""
from models.base_model import BaseModel

class City(BaseModel):
    """city class for place class"""

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """constructor for City class

        arguments:
        name : str for city name
        state_id : str for city state id
        """
        super().__init__(*args, **kwargs)