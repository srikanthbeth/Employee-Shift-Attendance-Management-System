from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date

from database import get_db
from auth import admin_required
import crud

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# ==========================================
# Monthly Attendance Report
# ==========================================

@router.get("/monthly")
def monthly_report(
    month: int,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    return crud.monthly_report(
        db,
        month,
        page,
        limit
    )


# ==========================================
# Filter Attendance
# ==========================================

@router.get("/filter")
def filter_attendance(
    employee_id: int = None,
    department: str = None,
    attendance_date: date = None,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):

    return crud.filter_attendance(
        db,
        employee_id,
        department,
        attendance_date
    )