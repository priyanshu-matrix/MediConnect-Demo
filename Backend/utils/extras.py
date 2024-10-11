import random
from string import digits


def get_random_id(length: int) -> int:
    return "".join(random.choices(digits, k=length))
