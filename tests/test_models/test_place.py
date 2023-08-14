#!/usr/bin/python3
"""this is test files"""
from models.place import Place


class TestPlace(unittest.TestCase):
    """test"""

    def test_init(self):
        """test"""
        obj = Place()
        self.assertIsInstance(obj, place, "faile")
        self.assertIsInstance(obj.city_id, str, "faile")
        self.assertIsInstance(obj.name, str, "faile")
        self.assertIsInstance(obj.description, str, "faile")
        self.assertIsInstance(obj.number_rooms, int, "faile")
        self.assertIsInstance(obj.number_bathrooms, int, "faile")
        self.assertIsInstance(obj.max_guest, int, "faile")
        self.assertIsInstance(obj.price_by_night, int, "faile")
        self.assertIsInstance(obj.latitude, float, "faile")
        self.assertIsInstance(obj.amenity_ids, str, "faile")
        self.assertIsInstance(obj.longitude, str, "faile")
