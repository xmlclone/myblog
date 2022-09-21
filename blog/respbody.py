import typing

from pydantic import BaseModel


class StatusResponse(BaseModel):
    '''
    0: success
    '''
    status_code: int = 0
    message: str = 'success'

class TokenResponse(BaseModel):
    status: StatusResponse = StatusResponse()
    token: str
