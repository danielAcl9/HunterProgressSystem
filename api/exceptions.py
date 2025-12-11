"""Custom exceptions for the API module."""

from fastapi import HTTPException, status

class QuestNotFoundException(HTTPException):
    """Exception for quest not found."""

    def __init__(self, quest_id: str):
        super().__init__(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Quest with id '{quest_id}' not found"
        )

class HunterNotFoundException(HTTPException):
    """Exception for hunter not found"""
    def __init__(self):
        super().__init__(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Hunter profile not found"
        )

class ValidationException(HTTPException):
    """Exception for validation errors."""
    def __init__(self, message: str):
        super().__init__(
            status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail = message
        )

class InternalServerException(HTTPException):
    """Exception for internal server errors."""
    def __init__(self, message: str = "Internal server error"):
        super().__init__(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = message
        )