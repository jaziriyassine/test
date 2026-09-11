# Activation Security Tester — GitHub Actions

A safe Python test harness for an activation-code API that you own or are explicitly authorized to test.

## What it does
- Validates 16-digit activation-code format.
- Rejects values below `1111111111111111`.
- Runs automated unit tests in GitHub Actions.
- Optionally runs one authorized API smoke test when `API_URL` is configured as a GitHub secret.
- Does not brute-force or infinitely guess activation codes.

## Local setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
python -m unittest discover -s tests -v
```

Run the local test harness:
```bash
python main.py
```

## GitHub Actions

Push this repository to GitHub. The workflow in `.github/workflows/test.yml` runs automatically on pushes and pull requests.

For an optional API smoke test, add a repository secret:

- `API_URL` — your authorized test/staging endpoint

Then manually run the workflow and enable the smoke test input.

Never commit real activation codes, API tokens, passwords, or private credentials.
