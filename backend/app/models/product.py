from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    # id must be optional
    # when a product is posted it wont have an id until one is generated in the backend
    id: Optional[int] = None
    title: str
    price: float
    description: str
    image: str
    category: str
