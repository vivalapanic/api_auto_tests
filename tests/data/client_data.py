import pytest
from faker import Faker
fake = Faker()
import random
from datetime import timedelta, datetime

payload = {
    "firstname": "Jim",
    "lastname": "Brown",
     "totalprice": 111,
     "depositpaid": True,
     "bookingdates": {
          "checkin": "2018-01-01",
           "checkout": "2019-01-01"
     },
     "additionalneeds": "Breakfast"
}

update_payload = {
    "firstname": "Anna",
    "lastname": "Smith",
     "totalprice": 222,
     "depositpaid": False,
     "bookingdates": {
          "checkin": "2020-01-01",
           "checkout": "2021-01-01"
     },
     "additionalneeds": "SPA"
}

create_payloads = [
{
    "firstname": "Nikol",
    "lastname": "Smith",
     "totalprice": 222,
     "depositpaid": False,
     "bookingdates": {
          "checkin": "2020-11-25",
           "checkout": "2021-01-01"
     },
     "additionalneeds": "SPA"
},
{
    "firstname": "Anna",
    "lastname": "Jonson",
     "totalprice": 0,
     "depositpaid": True,
     "bookingdates": {
          "checkin": "2022-12-31",
           "checkout": "2023-01-01"
     },
     "additionalneeds": None
}
]


invalid_payloads = [
{
    "firstname": None,
    "lastname": "Smith",
     "totalprice": 222,
     "depositpaid": False,
     "bookingdates": {
          "checkin": "2020-11-25",
           "checkout": "2021-01-01"
     },
     "additionalneeds": "SPA"
},
{
    "firstname": "Anna",
    "lastname": None,
     "totalprice": 0,
     "depositpaid": True,
     "bookingdates": {
          "checkin": "2022-12-31",
           "checkout": "2023-01-01"
     },
     "additionalneeds": None
},
{
    "firstname": "Anna",
    "lastname": "Jonson",
     "totalprice": None,
     "depositpaid": True,
     "bookingdates": {
          "checkin": "2022-12-31",
           "checkout": "2023-01-01"
     },
     "additionalneeds": None
},
{
    "firstname": "Anna",
    "lastname": "Jonson",
     "totalprice": 0,
     "depositpaid": None,
     "bookingdates": {
          "checkin": "2022-12-31",
           "checkout": "2023-01-01"
     },
     "additionalneeds": None
},
{
    "firstname": "Anna",
    "lastname": "Jonson",
     "totalprice": 0,
     "depositpaid": True,
     "bookingdates": None,
     "additionalneeds": None
}
]

# checkins = ["2024-01-01", "2024-01-05"]
# checkouts = ["2024-01-02", "2024-01-10"]

# def generate_pairs():
#     pairs = []
#     for checkin in checkins:
#         for checkout in checkouts:
#             checkin_date = datetime.fromisoformat(checkin)
#             checkout_date = datetime.fromisoformat(checkout)
#
#             if checkout_date > checkin_date:
#                 pairs.append(pytest.param(checkin, checkout))
#     return pairs

def generate_pairs(n=5):
    pairs = []
    for _ in range(n):
        checkin = fake.date_between(start_date='-2y', end_date='today')
        checkout = checkin + timedelta(days=random.randint(1, 10))

        pairs.append(
            pytest.param(
                str(checkin),
                str(checkout),
                id=f"{checkin} -> {checkout}"
            )
        )
    return pairs


def build_payload(checkin, checkout):
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": "Breakfast"
    }