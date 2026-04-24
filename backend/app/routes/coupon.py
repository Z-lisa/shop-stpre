from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app.models import Coupon, UserCoupon, User, UserCouponStatus, CouponStatus
from app.schemas import CouponResponse, UserCouponResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/coupons", tags=["优惠券"])


@router.get("", response_model=List[CouponResponse])
async def get_coupons(db: Session = Depends(get_db)):
    coupons = db.query(Coupon).filter(
        Coupon.status == CouponStatus.active,
        Coupon.valid_from <= datetime.now(),
        Coupon.valid_to >= datetime.now(),
        Coupon.issued_count < Coupon.total_count
    ).all()
    
    return coupons


@router.post("/{coupon_id}/claim")
async def claim_coupon(
    coupon_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    
    if not coupon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="优惠券不存在"
        )
    
    if coupon.status != CouponStatus.active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="优惠券已失效"
        )
    
    if coupon.issued_count >= coupon.total_count:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="优惠券已领完"
        )
    
    # 检查用户领取数量
    user_count = db.query(UserCoupon).filter(
        UserCoupon.user_id == current_user.id,
        UserCoupon.coupon_id == coupon_id
    ).count()
    
    if user_count >= coupon.per_user_limit:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="已达到领取上限"
        )
    
    # 创建用户优惠券
    user_coupon = UserCoupon(
        user_id=current_user.id,
        coupon_id=coupon_id,
        status=UserCouponStatus.unused,
        expires_at=coupon.valid_to
    )
    
    db.add(user_coupon)
    
    # 更新发放数量
    coupon.issued_count += 1
    
    db.commit()
    
    return {"message": "领取成功"}


@router.get("/my", response_model=List[UserCouponResponse])
async def get_my_coupons(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_coupons = db.query(UserCoupon).filter(
        UserCoupon.user_id == current_user.id
    ).all()
    
    return user_coupons


@router.get("/available", response_model=List[UserCouponResponse])
async def get_available_coupons(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_coupons = db.query(UserCoupon).filter(
        UserCoupon.user_id == current_user.id,
        UserCoupon.status == UserCouponStatus.unused,
        UserCoupon.expires_at >= datetime.now()
    ).all()
    
    return user_coupons
