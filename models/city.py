#!/usr/bin/python3
"""the module contain the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """The base model is the parent of  this class"""
    state_id = ""
    name = ""
