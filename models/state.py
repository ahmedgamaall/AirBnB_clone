#!/usr/bin/python3
"""state model"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class for place class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """constructor for State class

        arguments:
        name : str for state name
        """
        super().__init__(*args, **kwargs)

