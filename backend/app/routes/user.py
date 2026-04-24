from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/user", tags=["用户"])


@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/statistics")
async def get_statistics(current_user: User = Depends(get_current_user)):
    return {
        "total_spent": float(current_user.total_spent),
        "is_vip": current_user.is_vip,
        "vip_since": current_user.vip_since
    }
