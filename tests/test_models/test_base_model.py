#!/usr/bin/python3
"""ths is test module for base class"""
import uuid
from models.base_model import BaseModel
import sys
import unittest
from datetime import datetime
sys.path.append('..')


class TestBaseModel(unittest.TestCase):
    """the class"""
    def test_init(self):
        """method for __init__"""
        base_model = BaseModel()

        # Assert that id is a UUID
        self.assertIsInstance(base_model.id, str)

        # Assert that created_at and updated_at are datetime objects
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        """test the __Str__ method"""
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Assert that the string representation is formatted correctly
        expected_str = "[BaseModel] ({}) {}".format(
            str(base_model.id), str(base_model.__dict__))
        self.assertEqual(str(base_model), expected_str)

    def test_save(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Save and check that updated_at is updated
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_to_dict(self):
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Convert to dictionary
        base_model_dict = base_model.to_dict()

        # Assert that all expected keys are present in the dictionary
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, base_model_dict)

        # Assert that the values are converted to the expected string format
        self.assertEqual(base_model_dict['id'], str(base_model.id))
        self.assertEqual(
            base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(
            base_model_dict['updated_at'], base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
