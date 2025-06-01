from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    # id must be optional
    # when a product is posted it wont have an id until one is generated in the backend
    id: Optional[int] = None
    name: str
    age: int
    address: Optional[str] = None
    isAdmin: bool
