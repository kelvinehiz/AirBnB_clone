#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel as Base


class Review(Base):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Review object."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

