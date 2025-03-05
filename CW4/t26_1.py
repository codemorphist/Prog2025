import re
import requests
import openpyxl
from datetime import datetime

SYNOPTIC_URL = "https://sinoptik.ua"
SYNOPTIC_CITY = "Львов"


def get_html() -> str:
    url = f"{SYNOPTIC_URL}/погода-{SYNOPTIC_CITY}" 
    responce = requests.get(url) 
    return responce.text


def regex_parse():
    page_html = get_html()
    temp_div = re.findall("<div class=\"cFBF0wTW\">.*?<p>(.*?)</p>", page_html)
    cur_temp = re.findall("<p class=\"_6fYCPKSx\">(.*?)</p>", page_html)[0]
    min_temp, max_temp = temp_div[:2]

    return cur_temp, min_temp, max_temp


def update_data(filename: str = "temp_stat.xlsx"):

    wb = openpyxl.Workbook()
    
    ws = wb.active

    ws["A1"] = "Дата"
    ws["A2"]


    cur_data = datetime.today().strftime('%Y-%m-%d')
    cur_temp, min_temp, max_temp = regex_parse()
    ws.append([])

    wb.save(filename)


if __name__ == "__main__":
    update_data()
