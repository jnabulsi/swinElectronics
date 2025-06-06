from pathlib import Path
from app.services.AccountService import AccountService
from app.services.ProductService import ProductService 
from app.services.ShoppingCartService import ShoppingCartService
from app.services.OrderService import OrderService
from app.services.SalesReportService import SalesReportService


DATA_DIR = Path(__file__).parent / "data"

# File paths
ACCOUNTS_FILE = DATA_DIR / "accounts.json"
PRODUCTS_FILE = DATA_DIR / "products.json"
CART_FILE = DATA_DIR / "cart.json"
ORDERS_FILE = DATA_DIR / "orders.json"

# Service instances
acctService = AccountService(file_path=ACCOUNTS_FILE)
catalogService = ProductService(file_path=PRODUCTS_FILE)
cartService = ShoppingCartService(file_path=CART_FILE)
orderService = OrderService(file_path=ORDERS_FILE, catalog_path=PRODUCTS_FILE)
salesReportService = SalesReportService(orderService, catalogService)

