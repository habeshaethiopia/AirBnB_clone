#!/usr/bin/python3
"""the module contain the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """The base model is the parent of  this class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
