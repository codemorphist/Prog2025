"""
This module contains useful function to work with templates
based on Jinja2 package
"""

from app.settings import TEMPLATE_DIR
from app.utils import url

from jinja2 import Environment, FileSystemLoader, Template

jinja_env = Environment(loader = FileSystemLoader(TEMPLATE_DIR))

jinja_env.globals.update(zip=zip)
jinja_env.globals.update(urlpath=url)


def get_template(template: str) -> Template:
    return jinja_env.get_template(template)


def render(template: str, **kwargs):
    temp = get_template(template)
    return temp.render(**kwargs)
