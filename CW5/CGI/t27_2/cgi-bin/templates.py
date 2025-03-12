import os
from jinja2 import Environment, FileSystemLoader, Template

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PREV_DIR = "../"
TEMPLATE_DIR = "templates/"
TEMPLATES_DIR = os.path.join(CURRENT_DIR, PREV_DIR, TEMPLATE_DIR)

jinja_env = Environment(loader = FileSystemLoader(TEMPLATE_DIR))

def get_template(name: str) -> Template:
    return jinja_env.get_template(name)

