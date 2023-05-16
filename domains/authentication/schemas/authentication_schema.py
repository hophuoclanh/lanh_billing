from pydantic import BaseModel

class LoginSchema(BaseModel):
    user_name: str
    password: str

class LoginResponseSchema(BaseModel):
    access_token: str
    token_type: str = 'bearer'
