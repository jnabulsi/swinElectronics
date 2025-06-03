from pathlib import Path
from typing import List
from app.models.CartItemModel import CartItem
from app.storage.JsonStore import read_json, write_json  

class ShoppingCartService:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load_cart(self) -> List[CartItem]:
        return [CartItem(**item) for item in read_json(self.file_path)]

    def save_cart(self, items: List[CartItem]):
        write_json(self.file_path, [item.dict() for item in items])

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

