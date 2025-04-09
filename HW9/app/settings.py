"""
This file contains setting for app
"""

import os 

# Debug (if enabled show additional info in errors)
DEBUG = True 

# Base directory path
# Default dir where runserver.py
BASE_DIR = "." 

# Static files like: css, js, images
STATIC_DIR = "static"
STATIC_PATH = os.path.join(BASE_DIR, STATIC_DIR)

# Templates settings
TEMPLATE_DIR = "templates/"
TEMPLATES_DIR = os.path.join(BASE_DIR, TEMPLATE_DIR)

# Database settings
DB_DIR = "."
DB_NAME = "db.json"
DB_PATH = os.path.join(BASE_DIR, DB_DIR, DB_NAME)

