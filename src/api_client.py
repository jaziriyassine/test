import requests

from .config import API_URL, REQUEST_TIMEOUT
from .payload import create_payload


HEADERS = {
    "User-Agent": "SecurityTest/1.0",
    "Accept-Language": "fr",
    "Content-Type": "application/json",
}


def send_test_request(activation_code):
    """Send one authorized test request."""
    payload = create_payload(activation_code)

    return requests.post(
        API_URL,
        headers=HEADERS,
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
