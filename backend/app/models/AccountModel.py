from pydantic import BaseModel, EmailStr
from typing import Optional

class AccountIn(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int
    address: str

class AccountOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    isAdmin: bool = False

