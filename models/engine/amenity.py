#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel as Base


class Amenity(Base):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Amenity object."""
        super().__init__(*args, **kwargs)
        self.name = ""

