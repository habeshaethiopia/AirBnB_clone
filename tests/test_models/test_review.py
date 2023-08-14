#!/usr/bin/python3
"""this is test files"""
from models.review import Review

import unittest


class TestReview(unittest.TestCase):
    """test"""

    def test_init(self):
        """tests"""
        obj = Review()
        self.assertIsInstance(obj, Review, "faile")
        self.assertIsInstance(obj.place_id, str, "faile")
        self.assertIsInstance(obj.user_id, str, "faile")
        self.assertIsInstance(obj.text, str, "faile")


if __name__ == "__main__":
    unittest.main()
