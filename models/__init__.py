#!/usr/bin/python3
"""Script for share file_storage instance"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()