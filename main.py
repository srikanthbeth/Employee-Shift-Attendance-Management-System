from fastapi import FastAPI

from database import Base, engine

from routers import (
    auth,
    employees,
    shifts,
    attendance,
    reports
)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Create FastAPI App
app = FastAPI(
    title="Employee Shift & Attendance Management System",
    version="1.0.0",
    description="Employee Shift & Attendance Management API"
)

# Register Routers
app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(shifts.router)
app.include_router(attendance.router)
app.include_router(reports.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Shift & Attendance Management System"
    }