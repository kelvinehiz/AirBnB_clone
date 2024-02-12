#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel as Base


class City(Base):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initialize City object."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

