# backend/app/routes/reports.py
from fastapi import APIRouter, Query
from datetime import date
from typing import List, Optional
from app.models.sales import Sale

router = APIRouter()

# Temporary mock sales data
sales_db = [
    Sale(id=1, product_name="Mouse", quantity=2, price=25.5, sale_date=date(2024, 5, 1)),
    Sale(id=2, product_name="Keyboard", quantity=1, price=45.0, sale_date=date(2024, 5, 2)),
    Sale(id=3, product_name="Monitor", quantity=1, price=155.0, sale_date=date(2024, 5, 2)),
]

@router.get("/admin/sales-report", response_model=List[Sale])
def generate_report(start_date: Optional[date] = Query(None), end_date: Optional[date] = Query(None)):
    if start_date and end_date:
        return [sale for sale in sales_db if start_date <= sale.sale_date <= end_date]
    return sales_db
