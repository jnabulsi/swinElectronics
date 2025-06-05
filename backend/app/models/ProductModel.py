from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    title: str
    price: float
    description: str
    image: str
    category: str
    onSale: bool = False
    vendor: str

