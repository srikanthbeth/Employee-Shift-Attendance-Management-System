from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import (
    get_current_user,
    admin_required,
    employee_required
)


# ==========================
# Database Dependency
# ==========================

def get_database() -> Session:
    return Depends(get_db)


# ==========================
# Authentication Dependencies
# ==========================

def get_logged_in_user():
    return Depends(get_current_user)


def get_admin():
    return Depends(admin_required)


def get_employee():
    return Depends(employee_required)