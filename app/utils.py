"""Utility functions for the application."""


def sanitize_input(text):
    """Remove potentially dangerous characters from user input."""
    if not isinstance(text, str):
        return ""
    # Strip leading/trailing whitespace
    text = text.strip()
    # Basic length check
    if len(text) > 500:
        text = text[:500]
    return text


def format_response(data, status="ok"):
    """Format a standard API response."""
    return {
        "status": status,
        "data": data,
    }
