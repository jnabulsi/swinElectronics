from pydantic import BaseModel
from datetime import datetime

class SalesReportModel(BaseModel):
    order_id: int
    product_name: str
    quantity: int
    price: float
    date: datetime

