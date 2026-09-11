from .config import (
    DEVICE_ID,
    MAC_ADDRESS,
    APP_VERSION,
    DEVICE_MODEL,
    PLATFORM,
)
from .validator import is_valid_code


def create_payload(activation_code):
    """Create payload for an authorized test request."""
    if not is_valid_code(activation_code):
        raise ValueError("Invalid activation code")

    return {
        "activation_code": activation_code,
        "device_id": DEVICE_ID,
        "mac_address": MAC_ADDRESS,
        "app_version": APP_VERSION,
        "device_model": DEVICE_MODEL,
        "platform": PLATFORM,
    }
