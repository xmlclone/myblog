import typing

from pydantic import BaseModel, validator
from enum import Enum

from .models import BlogModel


class Code(Enum):
    SUCCESS = 0
    FAIL = 1
    AUTHFAIL = 406
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    

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
    token: str

class BlogResponse(Model):
    blogs: typing.List[BlogModel] = []
