#!/usr/bin/python3
"""this is test files"""
from models.user import User


class TestUser(unittest.TestCase):
    """test"""

    def test_init(self):
        """tests"""
        obj = User()
        self.assertIsInstance(obj, User, "faile")
        self.assertIsInstance(obj.email, str, "faile")
        self.assertIsInstance(obj.password, str, "faile")
        self.assertIsInstance(obj.first_name, str, "faile")
        self.assertIsInstance(obj.last_name, str, "faile")
