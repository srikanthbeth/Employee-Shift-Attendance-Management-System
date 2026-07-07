# Employee Shift & Attendance Management System

## Project Overview

The Employee Shift & Attendance Management System is a FastAPI-based backend application that helps organizations manage employees, shifts, and daily attendance records. The system includes JWT Authentication, Role-Based Authorization, CRUD operations, attendance management, reports, and search functionality.

---

## Objective

Develop a complete backend application using FastAPI that provides:

- JWT Authentication
- Role-Based Authorization
- Employee Management
- Shift Management
- Attendance Management
- Reports and Search
- Database Persistence
- Input Validation

---

## Tech Stack

- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Uvicorn
- Pytest

---

## Project Structure

```
employee_shift_attendance_system/

│── main.py
│── database.py
│── models.py
│── schemas.py
│── auth.py
│── dependencies.py
│── crud.py
│── utils.py
│── requirements.txt
│── README.md
│
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── employees.py
│   ├── shifts.py
│   ├── attendance.py
│   └── reports.py
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    ├── test_employee.py
    ├── test_shift.py
    └── test_attendance.py
```

---

## Installation

### Clone the Repository

```bash
git clone <repository_url>
cd employee_shift_attendance_system
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Server URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Redoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Authentication

The application uses JWT Authentication.

Roles Supported

- Admin
- Employee

---

## Authentication APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /auth/register | Register User |
| POST | /auth/login | Login User |

---

# Employee Management APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /employees | Create Employee |
| GET | /employees | Get All Employees |
| GET | /employees/{employee_id} | Get Employee by ID |
| PUT | /employees/{employee_id} | Update Employee |
| DELETE | /employees/{employee_id} | Soft Delete Employee |

---

# Shift Management APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /shifts | Create Shift |
| GET | /shifts | View All Shifts |
| PUT | /shifts/{shift_id} | Update Shift |

---

# Attendance APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /attendance | Mark Attendance |
| GET | /attendance | View All Attendance |
| GET | /attendance/{employee_id} | View Employee Attendance |
| PUT | /attendance/{attendance_id} | Update Attendance |

---

# Reports APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /reports/monthly | Monthly Attendance Report |
| GET | /reports/filter | Filter Attendance Records |

---

# Business Rules

- One employee can have only one attendance record per day.
- Check-out time must be greater than check-in time.
- Employee email must be unique.
- Phone number validation is enforced.
- Soft Delete is implemented for employees.
- JWT Authentication protects secured endpoints.
- Employees can view only their own attendance.
- Admin can manage all records.

---

# Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Role-Based Authorization
- Employee CRUD Operations
- Shift CRUD Operations
- Attendance Management
- Monthly Reports
- Attendance Filtering
- Pagination
- Pydantic Validation
- SQLite Database
- Swagger API Documentation
- Automated Testing using Pytest

---

# Database

Database Used

```
SQLite
```

Database File

```
employee.db
```

---

# Running Tests

Execute all tests

```bash
pytest
```

or

```bash
python -m pytest
```

---

# Dependencies

Main packages used

- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Passlib
- bcrypt
- python-jose
- python-multipart
- email-validator
- pytest
- httpx

---

# Future Improvements

- PostgreSQL Support
- Docker Integration
- Alembic Database Migrations
- Email Notifications
- Shift Assignment Automation
- Attendance Analytics Dashboard

---

# Author

**Name:** Srikanth Bethamcharla

---

# License

This project is developed for educational and assignment purposes.
