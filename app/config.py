"""Sample application config for AI code review testing."""


class AppConfig:
    """Application configuration with intentionally reviewable patterns."""

    DEBUG = True
    SECRET_KEY = "change-me-in-production"
    DATABASE_URL = "sqlite:///app.db"
    API_TIMEOUT = 30
    MAX_RETRIES = 3

    @staticmethod
    def get_api_headers():
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @staticmethod
    def validate_input(user_input):
        if not user_input:
            return False
        if len(user_input) > 1000:
            return False
        return True
