from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import Review, Product, User, Order, OrderStatus
from app.schemas import ReviewCreate, ReviewUpdate, ReviewResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/reviews", tags=["评价"])


@router.get("", response_model=List[ReviewResponse])
async def get_reviews(
    product_id: Optional[int] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    db: Session = Depends(get_db)
):
    query = db.query(Review).filter(Review.status == "approved")
    
    if product_id:
        query = query.filter(Review.product_id == product_id)
    
    # 分页
    offset = (page - 1) * page_size
    reviews = query.order_by(Review.created_at.desc()).offset(offset).limit(page_size).all()
    
    return reviews


@router.post("", response_model=ReviewResponse)
async def create_review(
    review_data: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # 检查商品是否存在
    product = db.query(Product).filter(Product.id == review_data.product_id).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="商品不存在"
        )
    
    # 如果有关联订单，检查订单状态
    if review_data.order_id:
        order = db.query(Order).filter(
            Order.id == review_data.order_id,
            Order.user_id == current_user.id
        ).first()
        
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="订单不存在"
            )
        
        if order.status != OrderStatus.completed:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="只能对已完成的订单进行评价"
            )
    
    db_review = Review(
        **review_data.model_dump(),
        user_id=current_user.id
    )
    
    db.add(db_review)
    
    # 更新商品评分
    product.review_count += 1
    all_reviews = db.query(Review).filter(Review.product_id == product.id).all()
    if all_reviews:
        avg_rating = sum(r.rating for r in all_reviews) / len(all_reviews)
        product.rating = round(avg_rating, 1)
    
    db.commit()
    db.refresh(db_review)
    
    return db_review


@router.put("/{review_id}", response_model=ReviewResponse)
async def update_review(
    review_id: int,
    review_data: ReviewUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    review = db.query(Review).filter(
        Review.id == review_id,
        Review.user_id == current_user.id
    ).first()
    
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="评价不存在"
        )
    
    update_data = review_data.model_dump(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(review, field, value)
    
    db.commit()
    db.refresh(review)
    
    return review


@router.delete("/{review_id}")
async def delete_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    review = db.query(Review).filter(
        Review.id == review_id,
        Review.user_id == current_user.id
    ).first()
    
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="评价不存在"
        )
    
    # 更新商品评分
    product = review.product
    product.review_count -= 1
    all_reviews = db.query(Review).filter(Review.product_id == product.id).all()
    if all_reviews:
        avg_rating = sum(r.rating for r in all_reviews) / len(all_reviews)
        product.rating = round(avg_rating, 1)
    else:
        product.rating = 0.0
    
    db.delete(review)
    db.commit()
    
    return {"message": "评价已删除"}


@router.post("/{review_id}/like")
async def like_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    review = db.query(Review).filter(Review.id == review_id).first()
    
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="评价不存在"
        )
    
    review.likes += 1
    db.commit()
    
    return {"message": "点赞成功"}
