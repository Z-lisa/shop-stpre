from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import CartItem, Product, User
from app.schemas import CartItemCreate, CartItemUpdate, CartItemResponse, CartResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/cart", tags=["购物车"])


@router.get("", response_model=CartResponse)
async def get_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    items = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.is_selected == True
    ).all()
    
    total_items = sum(item.quantity for item in items)
    total_price = sum(item.quantity * item.product.price for item in items)
    
    return {
        "items": items,
        "total_items": total_items,
        "total_price": total_price
    }


@router.post("/items", response_model=CartItemResponse)
async def add_to_cart(
    item_data: CartItemCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # 检查商品是否存在
    product = db.query(Product).filter(Product.id == item_data.product_id).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="商品不存在"
        )
    
    if product.status != "on_sale":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="商品已下架"
        )
    
    # 检查库存
    if product.stock < item_data.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="库存不足"
        )
    
    # 检查是否已存在
    existing_item = db.query(CartItem).filter(
        CartItem.user_id == current_user.id,
        CartItem.product_id == item_data.product_id,
        CartItem.size == item_data.size
    ).first()
    
    if existing_item:
        # 更新数量
        new_quantity = existing_item.quantity + item_data.quantity
        if product.stock < new_quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="库存不足"
            )
        existing_item.quantity = new_quantity
        existing_item.is_selected = True
        db_item = existing_item
    else:
        # 创建新项
        db_item = CartItem(
            **item_data.model_dump(),
            user_id=current_user.id
        )
        db.add(db_item)
    
    db.commit()
    db.refresh(db_item)
    
    return db_item


@router.put("/items/{item_id}", response_model=CartItemResponse)
async def update_cart_item(
    item_id: int,
    item_data: CartItemUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="购物车项不存在"
        )
    
    update_data = item_data.model_dump(exclude_unset=True)
    
    # 检查库存
    if "quantity" in update_data:
        if item.product.stock < update_data["quantity"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="库存不足"
            )
    
    for field, value in update_data.items():
        setattr(item, field, value)
    
    db.commit()
    db.refresh(item)
    
    return item


@router.delete("/items/{item_id}")
async def delete_cart_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="购物车项不存在"
        )
    
    db.delete(item)
    db.commit()
    
    return {"message": "已删除"}


@router.delete("")
async def clear_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db.query(CartItem).filter(
        CartItem.user_id == current_user.id
    ).delete()
    
    db.commit()
    
    return {"message": "购物车已清空"}


@router.post("/select/{item_id}")
async def toggle_select_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = db.query(CartItem).filter(
        CartItem.id == item_id,
        CartItem.user_id == current_user.id
    ).first()
    
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="购物车项不存在"
        )
    
    item.is_selected = not item.is_selected
    db.commit()
    
    return {"message": "操作成功"}


@router.post("/select-all")
async def select_all(
    select: bool = True,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db.query(CartItem).filter(
        CartItem.user_id == current_user.id
    ).update({"is_selected": select})
    
    db.commit()
    
    return {"message": "操作成功"}
