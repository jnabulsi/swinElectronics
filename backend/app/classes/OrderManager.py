import json
from pathlib import Path
from typing import List
from datetime import datetime

from app.classes.Order import Order
from app.classes.CartItem import CartItem
from app.classes.Product import Product
from app.classes.StoreCatalog import StoreCatalog

ORDERS_FILE = Path(__file__).parent.parent / "data" / "orders.json"

class OrderManager:
    def __init__(self, file_path: Path = ORDERS_FILE):
        self.file_path = file_path
        self.catalog = StoreCatalog()

    def load_orders(self) -> List[Order]:
        if not self.file_path.exists():
            return []
        with open(self.file_path) as f:
            return [Order(**o) for o in json.load(f)]

    def save_orders(self, orders: List[Order]):
        with open(self.file_path, "w") as f:
            json.dump([o.dict() for o in orders], f, indent=2, default=str)

    def create_order_from_cart(self, cart_items: List[CartItem]) -> Order:
        products = {p.id: p for p in self.catalog.load()}
        total = sum(products[item.productId].price * item.quantity for item in cart_items if item.productId in products)
        orders = self.load_orders()
        new_id = max((o.id for o in orders), default=0) + 1

        order = Order(
            id=new_id,
            items=cart_items,
            total=total,
            timestamp=datetime.utcnow()
        )

        orders.append(order)
        self.save_orders(orders)
        return order

