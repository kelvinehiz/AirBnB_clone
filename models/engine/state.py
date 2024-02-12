#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel as Base


class State(Base):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initialize State object."""
        super().__init__(*args, **kwargs)
        self.name = ""

