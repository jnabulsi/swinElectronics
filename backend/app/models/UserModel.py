from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None  # Add if you want to support IDs later
    name: str
    email: str
    age: int
    address: str
    isAdmin: bool = False

