import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    def __init__(self, name, surname, active=True):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = str(name[0].upper() + surname)
        self.id = generate_id()
