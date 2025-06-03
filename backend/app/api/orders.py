from fastapi import APIRouter, HTTPException
from typing import List
from app.services.ShoppingCartService import ShoppingCartService
from app.services.OrderService import OrderService
from app.models.OrderModel import Order
from app.config import cartService, orderService 

router = APIRouter()

@router.post("/orders/checkout", response_model=Order)
def complete_purchase():
    items = cartService.get_cart()

    if not items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = orderService.create_order_from_cart(items)
    cartService.clear_cart()
    return order

@router.get("/orders", response_model=List[Order])
def get_orders():
    return orderService.load_orders()

