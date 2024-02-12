#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel as Base


class User(Base):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """Initialize User object."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

