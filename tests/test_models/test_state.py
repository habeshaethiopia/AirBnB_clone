#!/usr/bin/python3
"""this is test files"""
from models.state import State


class TestState(unittest.TestCase):
    """test"""

    def test_init(self):
        """tests"""
        obj = State()
        self.assertIsInstance(obj, State, "faile")
        self.assertIsInstance(obj.name, str, "faile")
