def analyze_response(response):
    """Return basic response information without exposing secrets."""
    return {
        "status_code": response.status_code,
        "success": response.ok,
        "response_size": len(response.content),
    }
