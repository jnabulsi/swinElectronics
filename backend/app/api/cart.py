from fastapi import APIRouter, HTTPException
from typing import List
from app.classes.CartItem import CartItem
from app.classes.ShoppingCart import ShoppingCart

router = APIRouter()
cart = ShoppingCart()

@router.get("/cart", response_model=List[CartItem])
def get_cart():
    return cart.get_cart()

@router.post("/cart")
def add_to_cart(item: dict):
    product_id = item.get("productId")
    if not isinstance(product_id, int):
        raise HTTPException(status_code=400, detail="Invalid productId")
    cart.add_to_cart(product_id)
    return {"success": True}

@router.delete("/cart/{product_id}")
def remove_from_cart(product_id: int):
    cart.remove_from_cart(product_id)
    return {"success": True}

