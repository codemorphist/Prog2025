import os
from jinja2 import Environment, FileSystemLoader, Template

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = "templates/"
TEMPLATES_DIR = os.path.join(BASE_DIR, TEMPLATE_DIR)

jinja_env = Environment(loader = FileSystemLoader(TEMPLATE_DIR))


def get_template(template: str) -> Template:
    return jinja_env.get_template(template)


def render(template: str, **kwargs):
    temp = get_template(template)
    return temp.render(**kwargs)
