from dotenv import load_dotenv
import os
from fastapi.security import APIKeyHeader
from fastapi import Security, Depends
from typing import Annotated
from http_errors import UnauthorizedError, ForbiddenError


load_dotenv()

API_KEY = os.getenv('API_KEY')



api_key_header = APIKeyHeader(name='X-API-KEY', auto_error=False)


def validate_api_key(api_key: str = Security(api_key_header)) -> str:
    if api_key is None:
        print('MISSING API KEY HEADER')
        raise UnauthorizedError()
    
    if api_key != API_KEY:
        print('INVALID API KEY')
        raise ForbiddenError()
    
    return api_key



api_key_depends  = Annotated[str, Depends(validate_api_key)]