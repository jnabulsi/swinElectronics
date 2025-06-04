import json
from pathlib import Path
from app.models.product import Product
from typing import List

PRODUCTS_FILE = Path(__file__).parent.parent / "data" / "products.json"


def load_products():
    with open(PRODUCTS_FILE, "r") as f:
        return [Product(**p) for p in json.load(f)]

def save_products(products):
    with open(PRODUCTS_FILE, "w") as f:
        json.dump([p.dict() for p in products], f, indent=2)

def add_product(product_data: Product) -> Product:
    products = load_products()

    # Generate a new ID
    max_id = max((p.id for p in products), default=0)
    product_data.id = max_id + 1

    products.append(product_data)
    save_products(products)
    return product_data
