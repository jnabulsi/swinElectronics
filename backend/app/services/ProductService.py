from pathlib import Path
from typing import List, Optional
from app.models.ProductModel import Product
from app.storage.JsonStore import read_json, write_json  

class ProductService:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self) -> List[Product]:
        return [Product(**p) for p in read_json(self.file_path)]

    def save(self, products: List[Product]):
        write_json(self.file_path, [p.dict() for p in products])

    def add_product(self, product_data: Product) -> Product:
        products = self.load()
        max_id = max((p.id or 0 for p in products), default=0)
        product_data.id = max_id + 1
        products.append(product_data)
        self.save(products)
        return product_data

    def update_product(self, product_id: int, updated_data: Product) -> Optional[Product]:
        products = self.load()
        for i, product in enumerate(products):
            if product.id == product_id:
                updated_data.id = product_id
                products[i] = updated_data
                self.save(products)
                return updated_data
        return None

