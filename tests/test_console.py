#!/usr/python3
"""unittest for the AirBnB console"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """the tests for the console"""


if __name__ == "__main__":
    unittest.main()
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
