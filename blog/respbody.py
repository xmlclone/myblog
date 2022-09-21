import typing

from pydantic import BaseModel, validator
from enum import Enum


class Code(Enum):
    SUCCESS = 0
    AUTHFAIL = 406
    CONFLICT = 409
    

class Model(BaseModel):
    '''
    0: success
    '''
    code: Code = 0
    message: str = 'success'

    @validator('code')
    def code_validator(cls, code: Code):
        print(code.value)
        return code.value

class StatusResponse(Model):
    ''''''

class TokenResponse(Model):
    ''''''
    token: str
