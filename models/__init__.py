#!/usr/bin/python3
"""Script for share file_storage instance"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
