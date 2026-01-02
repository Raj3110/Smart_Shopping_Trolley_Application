import re
from datetime import datetime


def validate_card_number(card):
    return card.isdigit() and len(card) == 16


def validate_cvv(cvv):
    return cvv.isdigit() and len(cvv) == 3


def validate_expiry(expiry):
    if not re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", expiry):
        return False

    month, year = expiry.split("/")
    month = int(month)
    year = int("20" + year)

    now = datetime.now()
    expiry_date = datetime(year, month, 1)

    return expiry_date >= now.replace(day=1)
