from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    phone_number: str = None
    social_security_num: str = None
    username: str = None
    password: str = None
    email: str = None
    