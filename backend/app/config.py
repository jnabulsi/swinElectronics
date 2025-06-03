from pathlib import Path
from app.services.AccountService import AccountService
from app.services.UserService import UserService
from app.services.ProductService import ProductService 
from app.services.ShoppingCartService import ShoppingCartService
from app.services.OrderService import OrderService

DATA_DIR = Path(__file__).parent / "data"

# File paths
ACCOUNTS_FILE = DATA_DIR / "accounts.json"
USERS_FILE = DATA_DIR / "users.json"
PRODUCTS_FILE = DATA_DIR / "products.json"
CART_FILE = DATA_DIR / "cart.json"
ORDERS_FILE = DATA_DIR / "orders.json"

# Service instances
acctService = AccountService(file_path=ACCOUNTS_FILE)
userService = UserService(file_path=USERS_FILE)
catalogService = ProductService(file_path=PRODUCTS_FILE)
cartService = ShoppingCartService(file_path=CART_FILE)
orderService = OrderService(file_path=ORDERS_FILE, catalog_path=PRODUCTS_FILE)
