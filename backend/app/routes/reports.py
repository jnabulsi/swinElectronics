from fastapi import APIRouter, Query
from datetime import date
from typing import List, Optional
from app.models.sales import Sale

router = APIRouter()

# Temporary mock sales data
sales_db = [
    Sale(id=1, product_name="Wireless Mouse", quantity=4, price=29.99, sale_date=date(2024, 6, 1)),
    Sale(id=2, product_name="Wireless Mouse", quantity=6, price=29.99, sale_date=date(2024, 6, 3)),
    Sale(id=3, product_name="Mechanical Keyboard", quantity=7, price=89.99, sale_date=date(2024, 6, 2)),
    Sale(id=4, product_name="HD Monitor", quantity=3, price=199.99, sale_date=date(2024, 6, 4)),
]

@router.get("/admin/sales")
def generate_report(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    summary: bool = Query(False),
):
    # Filter sales by date if provided
    filtered_sales = sales_db
    if start_date and end_date:
        filtered_sales = [
            sale for sale in sales_db
            if start_date <= sale.sale_date <= end_date
        ]

    if not summary:
        # Return detailed sales list
        return filtered_sales

    # Prepare summary aggregation
    summary_dict = {}
    for sale in filtered_sales:
        if sale.product_name not in summary_dict:
            summary_dict[sale.product_name] = {"quantity": 0, "total_price": 0.0}
        summary_dict[sale.product_name]["quantity"] += sale.quantity
        summary_dict[sale.product_name]["total_price"] += sale.price * sale.quantity

    sales_summary = [
        {
            "product_name": product,
            "quantity": data["quantity"],
            "total_price": round(data["total_price"], 2),
        }
        for product, data in summary_dict.items()
    ]

    total_items = sum(item["quantity"] for item in sales_summary)
    total_value = sum(item["total_price"] for item in sales_summary)

    return {
        "sales_summary": sales_summary,
        "total_items_sold": total_items,
        "total_sales_value": round(total_value, 2),
    }


@router.get("/reports")
def get_reports():
    return {"message": "This is the reports endpoint"}
