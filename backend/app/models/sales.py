from pydantic import BaseModel
from datetime import datetime

class Sale(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    date: datetime

