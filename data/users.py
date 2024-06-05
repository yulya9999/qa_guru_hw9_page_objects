from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    email: str
    gender: str
    phone: str
    date_month: str
    date_day: str
    date_year: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str
