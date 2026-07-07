from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import admin_required
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
import crud

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# Create Employee (Admin Only)
@router.post("/", response_model=EmployeeResponse)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.create_employee(db, employee)


# Get All Employees
@router.get("/", response_model=list[EmployeeResponse])
def get_employees(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.get_employees(db)


# Get Employee By ID
@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.get_employee(db, employee_id)


# Update Employee
@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.update_employee(db, employee_id, employee)


# Soft Delete Employee
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.delete_employee(db, employee_id)