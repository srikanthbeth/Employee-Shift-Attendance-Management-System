from sqlalchemy.orm import Session
from sqlalchemy import extract
from fastapi import HTTPException

from models import User, Employee, Shift, Attendance
from schemas import (
    UserRegister,
    EmployeeCreate,
    EmployeeUpdate,
    ShiftCreate,
    ShiftUpdate,
    AttendanceCreate,
    AttendanceUpdate,
)
from utils import hash_password


# ==================================================
# USER
# ==================================================

def register_user(db: Session, user: UserRegister):

    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ==================================================
# EMPLOYEE
# ==================================================

def create_employee(db: Session, employee: EmployeeCreate):

    existing = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee email already exists")

    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


def get_employees(db: Session):
    return db.query(Employee).filter(Employee.is_active == True).all()


def get_employee(db: Session, employee_id: int):

    employee = db.query(Employee).filter(
        Employee.id == employee_id,
        Employee.is_active == True
    ).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


def update_employee(db: Session, employee_id: int, data: EmployeeUpdate):

    employee = get_employee(db, employee_id)

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)

    return employee


def delete_employee(db: Session, employee_id: int):

    employee = get_employee(db, employee_id)

    employee.is_active = False

    db.commit()

    return {"message": "Employee deleted successfully"}


# ==================================================
# SHIFT
# ==================================================

def create_shift(db: Session, shift: ShiftCreate):

    new_shift = Shift(**shift.model_dump())

    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)

    return new_shift


def get_shifts(db: Session):
    return db.query(Shift).all()


def update_shift(db: Session, shift_id: int, data: ShiftUpdate):

    shift = db.query(Shift).filter(
        Shift.id == shift_id
    ).first()

    if not shift:
        raise HTTPException(status_code=404, detail="Shift not found")

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(shift, key, value)

    db.commit()
    db.refresh(shift)

    return shift


# ==================================================
# ATTENDANCE
# ==================================================

def create_attendance(db: Session, attendance: AttendanceCreate):

    existing = db.query(Attendance).filter(
        Attendance.employee_id == attendance.employee_id,
        Attendance.date == attendance.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date"
        )

    if attendance.check_out <= attendance.check_in:
        raise HTTPException(
            status_code=400,
            detail="Check-out time must be greater than check-in time"
        )

    new_attendance = Attendance(**attendance.model_dump())

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


def get_all_attendance(db: Session):
    return db.query(Attendance).all()


def get_employee_attendance(db: Session, employee_id: int):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()


def update_attendance(
    db: Session,
    attendance_id: int,
    data: AttendanceUpdate
):

    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found"
        )

    updates = data.model_dump(exclude_unset=True)

    if (
        "check_in" in updates
        and "check_out" in updates
        and updates["check_out"] <= updates["check_in"]
    ):
        raise HTTPException(
            status_code=400,
            detail="Check-out must be greater than check-in"
        )

    for key, value in updates.items():
        setattr(attendance, key, value)

    db.commit()
    db.refresh(attendance)

    return attendance


# ==================================================
# REPORTS
# ==================================================

def monthly_report(
    db: Session,
    month: int,
    page: int = 1,
    limit: int = 10
):

    offset = (page - 1) * limit

    return (
        db.query(Attendance)
        .filter(extract("month", Attendance.date) == month)
        .offset(offset)
        .limit(limit)
        .all()
    )


def filter_attendance(
    db: Session,
    employee_id: int = None,
    department: str = None,
    date=None
):

    query = db.query(Attendance).join(Employee)

    if employee_id:
        query = query.filter(
            Attendance.employee_id == employee_id
        )

    if department:
        query = query.filter(
            Employee.department == department
        )

    if date:
        query = query.filter(
            Attendance.date == date
        )

    return query.all()