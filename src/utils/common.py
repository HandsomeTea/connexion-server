import random
import string


def random_string(len: int = 8):
    return ''.join(random.sample(string.ascii_letters + string.digits, len))
