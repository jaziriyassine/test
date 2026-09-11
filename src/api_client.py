import requests

from .config import API_URL, REQUEST_TIMEOUT
from .payload import create_payload


HEADERS = {
    "User-Agent": "ActivationSecurityTester/1.0",
    "Accept-Language": "fr",
    "Content-Type": "application/json",
}


def send_test_request(activation_code):
    """Send exactly one authorized smoke-test request."""
    if not API_URL.startswith(("https://", "http://")):
        raise ValueError("API_URL must be an HTTP(S) URL")

    payload = create_payload(activation_code)

    return requests.post(
        API_URL,
        headers=HEADERS,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
