#!/usr/bin/python3
"""the module contain the User class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The base model is the parent of  this class"""
    place_id = ""
    user_id = ""
    text = ""
