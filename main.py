from src.generator import generate_test_code
from src.validator import is_valid_code
from src.api_client import send_test_request
from src.analyzer import analyze_response


def main():
    print("=" * 50)
    print(" Activation Security Tester")
    print("=" * 50)

    code = generate_test_code()
    print(f"\nGenerated test code: {code}")

    if not is_valid_code(code):
        print("ERROR: Generated code is invalid.")
        return

    print("Code validation: OK")
    print("Sending ONE authorized test request...")

    try:
        response = send_test_request(code)
        result = analyze_response(response)

        print("\n--- Result ---")
        print(f"HTTP Status : {result['status_code']}")
        print(f"Success     : {result['success']}")
        print(f"Response    : {result['response_size']} bytes")

        print("\n--- Response ---")
        print(response.text)

    except Exception as error:
        print(f"\nRequest error: {error}")


if __name__ == "__main__":
    main()
