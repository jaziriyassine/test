from src.generator import generate_test_code
from src.validator import is_valid_code


def main():
    print("=" * 55)
    print(" Activation Security Tester")
    print("=" * 55)

    code = generate_test_code()

    print(f"Generated test code: {code}")
    print(f"Validation result: {is_valid_code(code)}")

    print("\nThis local harness does not brute-force activation codes.")
    print("Use the GitHub Actions workflow for automated authorized tests.")


if __name__ == "__main__":
    main()
