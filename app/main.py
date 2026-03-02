"""Sample application entry point."""

from config import AppConfig


def process_request(data):
    """Process incoming request data."""
    if not AppConfig.validate_input(data):
        return {"error": "Invalid input"}

    result = {
        "status": "ok",
        "processed": True,
        "data": data,
    }
    return result


def main():
    print("AI CI/CD Firing Range - Sample App")
    print(f"Debug mode: {AppConfig.DEBUG}")


if __name__ == "__main__":
    main()
