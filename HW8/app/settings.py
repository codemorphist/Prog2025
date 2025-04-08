import os 

# Base directory path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Templates settings
TEMPLATE_DIR = "templates/"
TEMPLATES_DIR = os.path.join(BASE_DIR, TEMPLATE_DIR)


# Database settings
DB_DIR = "."
DB_NAME = "db.json"
DB_PATH = os.path.join(BASE_DIR, DB_DIR, DB_NAME)
