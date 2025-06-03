from pydantic import BaseModel

class CartItem(BaseModel):
    productId: int
    quantity: int

