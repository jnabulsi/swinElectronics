class Sale:
    def __init__(self, order_id, product_name, quantity, price, date):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.date = date

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "price": self.price,
            "date": self.date
        }
