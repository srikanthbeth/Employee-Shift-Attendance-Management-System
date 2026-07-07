from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import admin_required
from schemas import ShiftCreate, ShiftUpdate, ShiftResponse
import crud

router = APIRouter(
    prefix="/shifts",
    tags=["Shift Management"]
)


# Create Shift (Admin Only)
@router.post("/", response_model=ShiftResponse)
def create_shift(
    shift: ShiftCreate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.create_shift(db, shift)


# Get All Shifts
@router.get("/", response_model=list[ShiftResponse])
def get_shifts(
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.get_shifts(db)


# Update Shift
@router.put("/{shift_id}", response_model=ShiftResponse)
def update_shift(
    shift_id: int,
    shift: ShiftUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return crud.update_shift(db, shift_id, shift)