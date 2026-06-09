from typing import Any, Optional
from fastapi import HTTPException


class NotFoundError(HTTPException):
    
    def __init__(self, status_code: int, code: str, field: Optional[str]=None, detail: Any = None) -> None:
        self.code = code
        self.field = field
        super().__init__(status_code, detail)
        