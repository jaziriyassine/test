import random

from .config import CODE_LENGTH, MIN_CODE


def generate_test_code():
    """Generate one valid 16-digit test value locally."""
    minimum = max(MIN_CODE, 10 ** (CODE_LENGTH - 1))
    maximum = (10 ** CODE_LENGTH) - 1
    return str(random.randint(minimum, maximum))
