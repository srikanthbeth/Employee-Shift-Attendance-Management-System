from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from auth import admin_required, get_current_user
from models import User
from schemas import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse
)
import crud

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# ====================================
# Mark Attendance (Admin Only)
# ====================================

@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.create_attendance(db, attendance)


# ====================================
# View All Attendance (Admin Only)
# ====================================

@router.get("/", response_model=list[AttendanceResponse])
def get_all_attendance(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.get_all_attendance(db)


# ====================================
# Employee/Admin View Attendance
# ====================================

@router.get("/{employee_id}", response_model=list[AttendanceResponse])
def get_employee_attendance(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Employee can only see their own attendance
    if current_user.role.lower() == "employee":

        employee = db.query(User).filter(
            User.username == current_user.username
        ).first()

        if employee.id != employee_id:
            raise HTTPException(
                status_code=403,
                detail="You can only view your own attendance."
            )

    return crud.get_employee_attendance(db, employee_id)


# ====================================
# Update Attendance (Admin Only)
# ====================================

@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.update_attendance(
        db,
        attendance_id,
        attendance
    )