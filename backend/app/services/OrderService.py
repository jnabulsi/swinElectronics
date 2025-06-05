from pathlib import Path
from typing import List
from datetime import datetime
from zoneinfo import ZoneInfo

from app.models.OrderModel import Order
from app.models.CartItemModel import CartItem
from app.services.ProductService import ProductService 
from app.storage.JsonStore import read_json, write_json  

class OrderService:
    def __init__(self, file_path: Path, catalog_path: Path):
        self.file_path = file_path
        self.catalog = ProductService(catalog_path)

    def load_orders(self) -> List[Order]:
        return [Order(**o) for o in read_json(self.file_path)]

    def save_orders(self, orders: List[Order]):
        write_json(self.file_path, [o.dict() for o in orders])

    def create_order_from_cart(self, cart_items: List[CartItem]) -> Order:
        products = {p.id: p for p in self.catalog.load()}
        total = sum(
            products[item.productId].price * item.quantity
            for item in cart_items
            if item.productId in products
        )
        orders = self.load_orders()
        new_id = max((o.id for o in orders), default=0) + 1

        melbourne_time = datetime.now(ZoneInfo("Australia/Melbourne"))

        order = Order(
            id=new_id,
            items=cart_items,
            total=total,
            timestamp=melbourne_time.isoformat()
        )

        orders.append(order)
        self.save_orders(orders)
        return order

