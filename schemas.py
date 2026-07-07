from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time


# ==========================
# User Schemas
# ==========================

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# ==========================
# Employee Schemas
# ==========================

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=10)
    department: str
    designation: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=10, max_length=10)
    department: Optional[str] = None
    designation: Optional[str] = None
    is_active: Optional[bool] = None


class EmployeeResponse(EmployeeBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


# ==========================
# Shift Schemas
# ==========================

class ShiftBase(BaseModel):
    shift_name: str
    start_time: time
    end_time: time
    shift_type: str


class ShiftCreate(ShiftBase):
    pass


class ShiftUpdate(BaseModel):
    shift_name: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    shift_type: Optional[str] = None


class ShiftResponse(ShiftBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# Attendance Schemas
# ==========================

class AttendanceBase(BaseModel):
    employee_id: int
    shift_id: int
    date: date
    check_in: time
    check_out: time
    attendance_status: str


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    shift_id: Optional[int] = None
    date: Optional[date] = None
    check_in: Optional[time] = None
    check_out: Optional[time] = None
    attendance_status: Optional[str] = None


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True