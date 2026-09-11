from .config import CODE_LENGTH, MIN_CODE


def is_valid_code(code):
    """Validate activation-code format and minimum value."""
    if not isinstance(code, str):
        return False
    if len(code) != CODE_LENGTH:
        return False
    if not code.isdigit():
        return False
    return int(code) >= MIN_CODE
