"""
This file contains setting for app
"""

import os 

# Base directory path
BASE_DIR = "." 

# Templates settings
TEMPLATE_DIR = "templates/"
TEMPLATES_DIR = os.path.join(BASE_DIR, TEMPLATE_DIR)


# Database settings
DB_DIR = "."
DB_NAME = "db.json"
DB_PATH = os.path.join(BASE_DIR, DB_DIR, DB_NAME)
