import random

from .config import CODE_LENGTH, MIN_CODE


def generate_test_code():
    """Generate a valid 16-digit test code."""
    minimum = max(MIN_CODE, 10 ** (CODE_LENGTH - 1))
    maximum = (10 ** CODE_LENGTH) - 1
    return str(random.randint(minimum, maximum))
