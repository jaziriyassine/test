# Activation Security Tester

Safe test harness for an activation-code API that you own or are explicitly authorized to test.

## Features
- 16-digit code validation
- Rejects values below `1111111111111111`
- Separate generator, validator, payload and API client
- Sends only a single authorized test request per run
- No brute-force or infinite guessing loop

## Setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set your authorized test endpoint in `src/config.py`, then run:

```bash
python main.py
```
