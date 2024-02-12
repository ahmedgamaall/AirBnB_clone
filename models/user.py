#!usr/bin/python3
"""user model"""
from models.base_model import BaseModel

class User(BaseModel):
    """user class for place class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """constructor for User class

        arguments:
        email : str for user name
        password : str for user name
        first_name : str for user name
        last_name : str for user name
        """
        super().__init__(*args, **kwargs)