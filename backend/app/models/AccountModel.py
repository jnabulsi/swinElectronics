from pydantic import BaseModel, EmailStr
from typing import Optional

class AccountIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str

class AccountOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: str
    isAdmin: bool = False

class LoginIn(BaseModel):
    email: EmailStr
    password: str