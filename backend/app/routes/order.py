from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
from decimal import Decimal
import random
import string
from app.database import get_db
from app.models import Order, OrderItem, OrderStatus, User, Address, Product, UserCoupon, UserCouponStatus, Coupon
from app.schemas import OrderCreate, OrderResponse, OrderStatusEnum
from app.dependencies import get_current_user

router = APIRouter(prefix="/orders", tags=["订单"])


def generate_order_no() -> str:
    """生成订单号"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.digits, k=6))
    return f"{timestamp}{random_str}"


@router.get("", response_model=List[OrderResponse])
async def get_orders(
    status_filter: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Order).filter(Order.user_id == current_user.id)
    
    if status_filter:
        query = query.filter(Order.status == status_filter)
    
    # 分页
    offset = (page - 1) * page_size
    orders = query.order_by(Order.created_at.desc()).offset(offset).limit(page_size).all()
    
    return orders


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order_detail(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="订单不存在"
        )
    
    return order


@router.post("", response_model=OrderResponse)
async def create_order(
    order_data: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # 获取地址
    address = db.query(Address).filter(
        Address.id == order_data.address_id,
        Address.user_id == current_user.id
    ).first()
    
    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="地址不存在"
        )
    
    # 检查商品和库存
    items_data = []
    total_amount = Decimal("0")
    original_amount = Decimal("0")
    
    for item_data in order_data.items:
        product = db.query(Product).filter(Product.id == item_data.product_id).first()
        
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"商品 {item_data.product_id} 不存在"
            )
        
        if product.status != "on_sale":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"商品 {product.name} 已下架"
            )
        
        # 检查库存（考虑尺码）
        if product.stock < item_data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"商品 {product.name} 库存不足"
            )
        
        items_data.append({
            "product": product,
            "quantity": item_data.quantity,
            "size": item_data.size
        })
        
        subtotal = product.price * item_data.quantity
        total_amount += subtotal
        original_amount += subtotal
    
    # 应用优惠券
    discount_amount = Decimal("0")
    coupon = None
    
    if order_data.coupon_id:
        user_coupon = db.query(UserCoupon).filter(
            UserCoupon.id == order_data.coupon_id,
            UserCoupon.user_id == current_user.id,
            UserCoupon.status == UserCouponStatus.unused
        ).first()
        
        if not user_coupon:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="优惠券不可用"
            )
        
        coupon_obj = user_coupon.coupon
        
        # 检查优惠券使用条件
        if total_amount < coupon_obj.min_amount:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"订单金额未达到优惠券使用门槛（满{coupon_obj.min_amount}可用）"
            )
        
        # 计算优惠金额
        if coupon_obj.type == "fixed":
            discount_amount = coupon_obj.discount_value
        elif coupon_obj.type == "percentage":
            discount_amount = total_amount * (coupon_obj.discount_value / 100)
            if coupon_obj.max_discount:
                discount_amount = min(discount_amount, coupon_obj.max_discount)
        
        coupon = user_coupon
    
    # 应用 VIP 折扣
    vip_discount = Decimal("1.00")
    if current_user.is_vip:
        vip_discount = Decimal("0.85")
        vip_discount_amount = total_amount * (1 - vip_discount)
        discount_amount += vip_discount_amount
    
    # 确保最终金额不为负
    final_amount = max(total_amount - discount_amount, Decimal("0"))
    
    # 创建订单
    order_no = generate_order_no()
    
    order = Order(
        order_no=order_no,
        user_id=current_user.id,
        address_snapshot={
            "name": address.name,
            "phone": address.phone,
            "province": address.province,
            "city": address.city,
            "district": address.district,
            "detail": address.detail
        },
        total_amount=final_amount,
        original_amount=original_amount,
        discount_amount=discount_amount,
        vip_discount=vip_discount,
        coupon_id=coupon.id if coupon else None,
        note=order_data.note,
        status=OrderStatus.pending,
        auto_ship_at=datetime.now() + timedelta(minutes=5)  # 5 分钟后自动发货
    )
    
    db.add(order)
    db.flush()  # 获取 order.id
    
    # 创建订单项
    for item_data in items_data:
        product = item_data["product"]
        quantity = item_data["quantity"]
        size = item_data["size"]
        
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            product_name=product.name,
            product_cover=product.cover_image,
            size=size,
            quantity=quantity,
            unit_price=float(product.price),
            subtotal=float(product.price * quantity)
        )
        db.add(order_item)
        
        # 扣减库存
        product.stock -= quantity
    
    # 使用优惠券
    if coupon:
        coupon.status = UserCouponStatus.used
        coupon.used_at = datetime.now()
        coupon.order_id = order.id
    
    db.commit()
    db.refresh(order)
    
    return order


@router.post("/{order_id}/pay")
async def pay_order(
    order_id: int,
    pay_method: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="订单不存在"
        )
    
    if order.status != OrderStatus.pending:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="订单状态不允许支付"
        )
    
    # 更新订单状态
    order.status = OrderStatus.paid
    order.pay_method = pay_method
    order.pay_time = datetime.now()
    
    # 更新用户消费金额
    current_user.total_spent += order.total_amount
    
    # 检查是否达到 VIP 条件
    if not current_user.is_vip and current_user.total_spent >= 500:
        current_user.is_vip = True
        current_user.vip_since = datetime.now()
    
    db.commit()
    
    return {"message": "支付成功", "order_id": order.id}


@router.post("/{order_id}/cancel")
async def cancel_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="订单不存在"
        )
    
    if order.status != OrderStatus.pending:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="只能取消待支付订单"
        )
    
    # 恢复库存
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            product.stock += item.quantity
    
    # 退还优惠券
    if order.coupon_id:
        user_coupon = db.query(UserCoupon).filter(
            UserCoupon.id == order.coupon_id
        ).first()
        if user_coupon:
            user_coupon.status = UserCouponStatus.unused
            user_coupon.used_at = None
            user_coupon.order_id = None
    
    order.status = OrderStatus.cancelled
    order.cancel_time = datetime.now()
    
    db.commit()
    
    return {"message": "订单已取消"}


@router.post("/{order_id}/confirm")
async def confirm_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == current_user.id
    ).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="订单不存在"
        )
    
    if order.status != OrderStatus.shipped:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="只能确认已发货订单"
        )
    
    order.status = OrderStatus.completed
    order.complete_time = datetime.now()
    
    db.commit()
    
    return {"message": "订单已完成"}
