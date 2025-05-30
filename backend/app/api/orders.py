from fastapi import APIRouter, HTTPException
from typing import List
from app.classes.ShoppingCart import ShoppingCart
from app.classes.OrderManager import OrderManager
from app.classes.Order import Order

router = APIRouter()

@router.post("/orders/checkout", response_model=Order)
def complete_purchase():
    cart = ShoppingCart()
    items = cart.get_cart()

    if not items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    manager = OrderManager()
    order = manager.create_order_from_cart(items)
    cart.clear_cart()
    return order

@router.get("/orders", response_model=List[Order])
def get_orders():
    manager = OrderManager()
    return manager.load_orders()

