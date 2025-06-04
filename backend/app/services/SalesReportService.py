from app.models.OrderModel import Order
from app.services.ProductService import ProductService
from app.services.OrderService import OrderService
from app.models.SalesReportModel import SalesReportModel
from datetime import datetime

class SalesReportService:
    def __init__(self, order_service: OrderService, product_service: ProductService):
        self.order_service = order_service
        self.product_service = product_service

    def generate_sales_report(self):
        orders = self.order_service.load_orders()
        products = {p.id: p for p in self.product_service.load()}
        report = []

        for order in orders:
            for item in order.items:
                product = products.get(item.productId)
                if product:

                    report.append(SalesReportModel(
                    order_id=order.id,
                    product_name=product.title,
                    quantity=item.quantity,
                    price=product.price,
                    date=order.timestamp
                    ))

        return report
