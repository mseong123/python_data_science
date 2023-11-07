import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default='Eagle', init=False)
    id: str = field(default_factory=generate_id, init=False)
