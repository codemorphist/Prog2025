import re
from urllib.request import urlopen
from urllib.parse import urljoin, quote


SYNOPTIC_URL = "https://sinoptik.ua"
SYNOPTIC_CITY = "Львов"


def get_html() -> str:
    url = f"{SYNOPTIC_URL}/погода-{SYNOPTIC_CITY}" 
    url = quote(url, safe=":/-", encoding="utf-8")
    print(url)
    responce = urlopen(url)
    return responce.read().decode()


def regex_parse():
    page_html = get_html()
    temp_div = re.findall("<div class=\"cFBF0wTW\">.*?<p>(.*?)</p>", page_html)
    cur_temp = re.findall("<p class=\"_6fYCPKSx\">(.*?)</p>", page_html)[0]
    min_temp, max_temp = temp_div[:2]

    print(cur_temp, min_temp, max_temp)


if __name__ == "__main__":
    regex_parse()
