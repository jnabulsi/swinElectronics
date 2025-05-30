import json
from pathlib import Path
from typing import List
from app.classes.Product import Product

PRODUCTS_FILE = Path(__file__).parent.parent / "data" / "products.json"

class StoreCatalog:
    def __init__(self, file_path: Path = PRODUCTS_FILE):
        self.file_path = file_path

    def load(self) -> List[Product]:
        if not self.file_path.exists():
            return []
        with open(self.file_path, "r") as f:
            return [Product(**p) for p in json.load(f)]

    def save(self, products: List[Product]):
        with open(self.file_path, "w") as f:
            json.dump([p.dict() for p in products], f, indent=2)

    def add_product(self, product_data: Product) -> Product:
        products = self.load()
        max_id = max((p.id or 0 for p in products), default=0)
        product_data.id = max_id + 1
        products.append(product_data)
        self.save(products)
        return product_data

