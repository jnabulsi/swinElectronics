import json
from pathlib import Path
from typing import List
from app.classes.CartItem import CartItem

CART_FILE = Path(__file__).parent.parent / "data" / "cart.json"

class ShoppingCart:
    def __init__(self, file_path: Path = CART_FILE):
        self.file_path = file_path

    def load_cart(self) -> List[CartItem]:
        if not self.file_path.exists():
            return []
        with open(self.file_path, "r") as f:
            return [CartItem(**item) for item in json.load(f)]

    def save_cart(self, items: List[CartItem]):
        with open(self.file_path, "w") as f:
            json.dump([item.dict() for item in items], f, indent=2)

    def get_cart(self) -> List[CartItem]:
        return self.load_cart()

    def add_to_cart(self, product_id: int):
        cart = self.load_cart()
        for item in cart:
            if item.productId == product_id:
                item.quantity += 1
                break
        else:
            cart.append(CartItem(productId=product_id, quantity=1))
        self.save_cart(cart)

    def remove_from_cart(self, product_id: int):
        cart = [item for item in self.load_cart() if item.productId != product_id]
        self.save_cart(cart)

    def clear_cart(self):
        self.save_cart([])

