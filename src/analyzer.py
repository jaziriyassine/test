def analyze_response(response):
    """Return a simple security-test result."""
    return {
        "status_code": response.status_code,
        "success": response.ok,
        "response_size": len(response.content),
    }
