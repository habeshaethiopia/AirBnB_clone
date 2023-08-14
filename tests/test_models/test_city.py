#!/usr/bin/python3
"""this is test files"""
from models.city import City


class TestCity(unittest.TestCase):
    """test"""

    def test_init(self):
        """is instance"""
        obj = City()
        self.assertIsInstance(obj, City, "faile")
        self.assertIsInstance(obj.state_id, str, "faile")
        self.assertIsInstance(obj.name, str, "faile")
