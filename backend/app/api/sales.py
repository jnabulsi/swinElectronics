from fastapi import APIRouter, HTTPException
from typing import List
from app.models.SalesReportModel import SalesReportModel
from app.config import salesReportService

router = APIRouter()

@router.get("/sales", response_model=List[SalesReportModel])
def get_sales_report():
    report = salesReportService.generate_sales_report()
    return report
