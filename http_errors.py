from typing import Any, Optional
from fastapi import HTTPException


class NotFoundError(HTTPException):
    
    def __init__(self, status_code: int, code: str, field: Optional[str]=None, detail: Any = None) -> None:
        self.code = code
        self.field = field
        super().__init__(status_code, detail)


class UnauthorizedError(HTTPException):
    
    def __init__(self, status_code: int=401, code: str='unauthorized', field: Optional[str]=None, detail: str = 'Invalid Key') -> None:
        self.code = code
        self.field = field
        super().__init__(status_code, detail) 
        
        
class ForbiddenError(HTTPException):
    
    def __init__(self, status_code: int=403, code: str='forbidden', field: Optional[str]=None, detail: str = "You don't have permission to access this endpoint") -> None:
        self.code = code
        self.field = field
        super().__init__(status_code, detail)