#!/home/x/Documents/Lectures/Prog2025/CW5/t27_2/venv/bin/python

import cgi
import os
import db
from templates import get_template

db.load_currency()

CGI_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = CGI_DIR

form = cgi.FieldStorage()

def convert(amount: float, currency: str) -> float:
    return amount * db.get_price(currency)

amount = float(form.getfirst("amount", "0.00"))
currency = form.getfirst("currency")
new_amount = convert(amount, currency)

from_currency, to_currency = currency.split("/")
res = f"{amount:.2f} {from_currency} -> {new_amount:.2f} {to_currency}"

index = get_template("index.html")
html = index.render(currency=db.get_currency(),
                    result=res)


print("Content-Type: text/html")
print()
print(html)
