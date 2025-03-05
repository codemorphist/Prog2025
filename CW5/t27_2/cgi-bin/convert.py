#!/home/x/Documents/Lectures/Prog2025/CW4/venv/bin/python

import cgi
import os

CGI_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = CGI_DIR

form = cgi.FieldStorage()

amount = float(form.getfirst("amount", "0.00"))
from_currency, to_currency = form.getfirst("currency", "USD/EUR").split("/")

print("Content-Type: text/html")
print()
print(f"{amount} {from_currency} -> {to_currency}")
