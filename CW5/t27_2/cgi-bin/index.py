#!/home/x/Documents/Lectures/Prog2025/CW5/t27_2/venv/bin/python

import cgi
import os
from templates import get_template
import db

db.load_currency()

index = get_template("index.html")
html = index.render(currency=db.get_currency())


print("Content-Type: text/html")
print()
print(html)
