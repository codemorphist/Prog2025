import os
import openpyxl

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PREV_DIR = "../"
DB_NAME = "db.xlsx"
DB_PATH = os.path.join(CURRENT_DIR, PREV_DIR, DB_NAME)

CURRENCY: dict[str, float] = {}

def load_currency():
    DB_WB = openpyxl.load_workbook(DB_PATH)
    DB_WS = DB_WB.active

    for row in DB_WS.iter_rows():
        from_cur, to_cur, price_cur = map(lambda r: r.value, row)
        
        try:
            cur = f"{from_cur}/{to_cur}"
            CURRENCY[cur] = float(price_cur)
        except: 
            continue


def get_currency():
    return list(CURRENCY.keys())


def get_price(currency: str) -> float:
    try:
        return CURRENCY[currency]
    except:
        return 0.0


if __name__ == "__main__":
    load_currency()
    print(get_currency())
