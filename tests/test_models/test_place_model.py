#!/usr/bin/python3
"""
Unittest for Place Class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestPlaceClass(unittest.TestCase):
    """
    test class for the Place Class
    """
    plc = Place()
    plc.name = "Entire villa in Purcellville"
    plc.id = "987-456-321"
    plc.city_id = "c-987789"
    plc.user_id = "u-654123"
    plc.description = "Spacious amazing top rated private resort for up to 16 guest."
    plc.number_rooms = 14
    plc.number_bathrooms = 6
    plc.max_guest = 16
    plc.price_by_night = 1166
    plc.latitude = 39.206603
    plc.longitude = -77.7541613
    plc.amenity_ids = ["am1", "am2"]

    def test_defaults(self):
        """test default values"""

        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, "")

    def test_object_without_kwargs(self):
        """
        create an object of Place class without kwargs
        """
        self.assertIsInstance(self.plc, Place)
        self.assertIsInstance(self.plc, BaseModel)
        self.assertIsInstance(self.plc.id, str)
        self.assertIsInstance(self.plc.name, str)
        self.assertIsInstance(self.plc.created_at, datetime)
        self.assertIsInstance(self.plc.updated_at, datetime)
        self.assertIsInstance(self.plc.city_id, str)
        self.assertIsInstance(self.plc.user_id, str)
        self.assertIsInstance(self.plc.description, str)
        self.assertIsInstance(self.plc.number_rooms, int)
        self.assertIsInstance(self.plc.number_bathrooms, int)
        self.assertIsInstance(self.plc.max_guest, int)
        self.assertIsInstance(self.plc.price_by_night, int)
        self.assertIsInstance(self.plc.latitude, float)
        self.assertIsInstance(self.plc.longitude, float)
        self.assertIsInstance(self.plc.amenity_ids, list)

        self.assertEqual(self.plc.name, "Entire villa in Purcellville")
        self.assertEqual(self.plc.id, "987-456-321")
        self.assertEqual(self.plc.city_id, "c-987789")
        self.assertEqual(self.plc.user_id, "u-654123")
        self.assertEqual(self.plc.description, "Spacious amazing top rated private resort for up to 16 guest.")
        self.assertEqual(self.plc.number_rooms, 14)
        self.assertEqual(self.plc.number_bathrooms, 6)
        self.assertEqual(self.plc.max_guest, 16)
        self.assertEqual(self.plc.price_by_night, 1166)
        self.assertEqual(self.plc.latitude, 39.206603)
        self.assertEqual(self.plc.longitude, -77.7541613)
        self.assertEqual(self.plc.amenity_ids, ["am1", "am2"])

    def test_object_with_kwargs(self):
        """
        create an object of Place class using kwargs
        """
        plc_data = {
            "id": "456-986-345",
            "name": "Farm stay in Hamilton",
            "city_id": "c-456986",
            "user_id": "u-123654",
            "description": "Gorgeous 150 acre equestrian Quaker style farmhouse built in 1856, fully renovated in 2019.",
            "number_rooms": 8,
            "number_bathrooms": 3,
            "max_guest": 10,
            "price_by_night": 459,
            "latitude": 40.3476,
            "longitude": 77.8790,
            "amenity_ids": ["am3", "am4"],
            "updated_at": "2024-02-08T12:00:00.563721",
            "created_at": "2024-02-11T12:00:00.563721"
        }

        n_plc = Place(**plc_data)
        self.assertIsInstance(n_plc, Place)
        self.assertIsInstance(n_plc, BaseModel)
        self.assertIsInstance(n_plc.id, str)
        self.assertIsInstance(n_plc.name, str)
        self.assertIsInstance(n_plc.created_at, datetime)
        self.assertIsInstance(n_plc.updated_at, datetime)
        self.assertIsInstance(n_plc.city_id, str)
        self.assertIsInstance(n_plc.user_id, str)
        self.assertIsInstance(n_plc.description, str)
        self.assertIsInstance(n_plc.number_rooms, int)
        self.assertIsInstance(n_plc.number_bathrooms, int)
        self.assertIsInstance(n_plc.max_guest, int)
        self.assertIsInstance(n_plc.price_by_night, int)
        self.assertIsInstance(n_plc.latitude, float)
        self.assertIsInstance(n_plc.longitude, float)
        self.assertIsInstance(n_plc.amenity_ids, list)

        self.assertEqual(n_plc.id, "456-986-345")
        self.assertEqual(n_plc.name, "Farm stay in Hamilton")
        self.assertEqual(n_plc.city_id, "c-456986")
        self.assertEqual(n_plc.user_id, "u-123654")
        self.assertEqual(n_plc.description, 
            "Gorgeous 150 acre equestrian Quaker style farmhouse built in 1856, fully renovated in 2019.")
        self.assertEqual(n_plc.number_rooms, 8)
        self.assertEqual(n_plc.number_bathrooms, 3)
        self.assertEqual(n_plc.max_guest, 10)
        self.assertEqual(n_plc.price_by_night, 459)
        self.assertEqual(n_plc.latitude, 40.3476)
        self.assertEqual(n_plc.longitude, 77.8790)
        self.assertEqual(n_plc.amenity_ids, ["am3", "am4"])

    def test_func_to_dict(self):
        """
            test to_dict class method
        """
        object_dict = self.plc.to_dict()
        expected_dic = self.plc.__dict__.copy()
        expected_dic["__class__"] = self.plc.__class__.__name__
        expected_dic["updated_at"] = self.plc.updated_at.isoformat()
        expected_dic["created_at"] = self.plc.created_at.isoformat()
        self.assertDictEqual(expected_dic, object_dict)

    def test_func_save(self):
        """"
            test save class method
        """
        bf_update = self.plc.updated_at
        self.plc.name = "Entire villa in Purcellville"
        self.plc.save()
        af_update = self.plc.updated_at
        self.assertNotEqual(bf_update, af_update)

    def test_func_str(self):
        """
            test str class method
        """
        s = self.plc.__class__.__name__
        exp_string = f"[{s}] ({self.plc.id}) {self.plc.__dict__}"
        self.assertEqual(self.plc.__str__(), exp_string)