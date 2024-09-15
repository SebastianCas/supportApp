from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    accessToken: str
    tokenType: str

class TokenData(BaseModel):
    username: str = None
    
class Users(BaseModel):
    userId: Optional[int] = None
    username: str
    password: str