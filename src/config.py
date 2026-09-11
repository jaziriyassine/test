import os

# Use only an API endpoint you own or are explicitly authorized to test.
API_URL = os.getenv(
    "API_URL",
    "https://your-test-api.example.com/api/v4/login",
)

CODE_LENGTH = 16
MIN_CODE = 1111111111111111
REQUEST_TIMEOUT = 10

DEVICE_ID = "TEST_DEVICE_001"
MAC_ADDRESS = "AA:BB:CC:DD:EE:FF"
APP_VERSION = "2.4.1"
DEVICE_MODEL = "AndroidTV"
PLATFORM = "android"
