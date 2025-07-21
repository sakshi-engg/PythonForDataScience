import re
from exception.invalid_input_exception import InvalidInputException

class ValidationService:

    @staticmethod
    def validate_email(email: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidInputException("Invalid email format.")

    @staticmethod
    def validate_phone(phone: str):
        if not re.match(r"^[0-9]{10}$", phone):
            raise InvalidInputException("Phone number must be 10 digits.")

    @staticmethod
    def validate_non_empty_string(value: str, field_name: str):
        if not value or not value.strip():
            raise InvalidInputException(f"{field_name} cannot be empty.")

    @staticmethod
    def validate_positive_number(value: float, field_name: str):
        if value < 0:
            raise InvalidInputException(f"{field_name} must be a positive number.")
