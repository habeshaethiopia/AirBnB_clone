#!/usr/bin/python3
"""the module contain the User class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """The base model is the parent of  this class"""
    cuty_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
