"""Custom exceptions."""
from fastapi import HTTPException


class DetailExists(HTTPException):
    def __init__(self, status_code: int, message: str, field: str):
        self.status_code = status_code
        self.message = message
        self.field = field
