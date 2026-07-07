from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

from database import Base


# ======================
# User Table
# ======================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="employee")



# ======================
# Employee Table
# ======================

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String, nullable=False)

    department = Column(String, nullable=False)

    designation = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)

    attendances = relationship(
        "Attendance",
        back_populates="employee"
    )



# ======================
# Shift Table
# ======================

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)

    shift_name = Column(String, nullable=False)

    start_time = Column(Time, nullable=False)

    end_time = Column(Time, nullable=False)

    shift_type = Column(String, nullable=False)

    attendances = relationship(
        "Attendance",
        back_populates="shift"
    )



# ======================
# Attendance Table
# ======================

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.id")
    )

    date = Column(Date, nullable=False)

    check_in = Column(Time, nullable=False)

    check_out = Column(Time)

    attendance_status = Column(String)

    employee = relationship(
        "Employee",
        back_populates="attendances"
    )

    shift = relationship(
        "Shift",
        back_populates="attendances"
    )