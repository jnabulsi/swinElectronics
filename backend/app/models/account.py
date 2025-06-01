from pydantic import BaseModel
from pathlib import Path
from typing import Optional

class Account(BaseModel):
    # id must be optional
    # when a product is posted it wont have an id until one is generated in the backend
    id: Optional[int] = None
    name: str
    age: int
    isAdmin: bool

ACCOUNTS_FILE = Path(__file__).parent.parent / "data" / "accounts.json"

def load_products():
    with open(PRODUCTS_FILE, "r") as f:
        return [Product(**p) for p in json.load(f)]