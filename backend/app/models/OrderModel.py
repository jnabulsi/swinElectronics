from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.models.CartItemModel import CartItem

class Order(BaseModel):
    id: int
    items: List[CartItem]
    total: float
    timestamp: datetime
