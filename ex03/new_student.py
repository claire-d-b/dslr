import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    return name[0].upper() + surname


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, repr=True)
    id: str = field(init=False, repr=True)

    """ In Python's dataclasses module, the __post_init__ method is a
    special method that gets called automatically after the dataclass's
    __init__ method has been executed.
    It allows you to perform additional initialization steps that need
    to occur after the initial setting of the dataclass's fields. """

    def __post_init__(self):
        """Set the _login attribute based on first_name and last_name
        after instance creation"""
        self.login = generate_login(self.name, self.surname)
        self.id = generate_id()
