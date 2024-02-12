#!/usr/bin/python3
"""Initialize the models directory."""
from models.engine.file_storage import FileStorage


file_storage = FileStorage()
file_storage.reload()

