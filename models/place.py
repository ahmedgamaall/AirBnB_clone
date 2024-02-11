#!/usr/bin/python3
"""Place model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        """constructor for Place class
        
        arguments:
            city_id : str for city id
            user_id : str for user id
            name : The name of the place
            description : A description of the place
            number_rooms : int for number of rooms in the place
            number_bathrooms : int number of bathrooms in the place
            max_guest : int maximum number of guests allowed in the place
            price_by_night : int price of per night for staying in the place
            latitude : float latitude of the place's location
            longitude : float longitude of the place's location
            amenity_ids : list IDs of amenities in the place
        """
        super().__init__(*args, **kwargs)

