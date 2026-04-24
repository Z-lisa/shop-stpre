from sqlalchemy import Column, Integer, String, DateTime, Boolean, DECIMAL, ForeignKey, Text, Enum, JSON, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class UserStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    banned = "banned"


class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class SizeType(str, enum.Enum):
    none = "none"
    clothing = "clothing"
    shoes = "shoes"


class ProductStatus(str, enum.Enum):
    on_sale = "on_sale"
    off_sale = "off_sale"
    out_of_stock = "out_of_stock"


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    completed = "completed"
    cancelled = "cancelled"


class PayMethod(str, enum.Enum):
    wechat = "wechat"
    alipay = "alipay"
    balance = "balance"


class CouponType(str, enum.Enum):
    fixed = "fixed"
    percentage = "percentage"


class CouponStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    exhausted = "exhausted"


class UserCouponStatus(str, enum.Enum):
    unused = "unused"
    used = "used"
    expired = "expired"


class ReviewStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(20), unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    avatar = Column(String(255))
    nickname = Column(String(50))
    gender = Column(Enum(Gender), default=Gender.other)
    total_spent = Column(DECIMAL(10, 2), default=0.00)
    is_vip = Column(Boolean, default=False)
    vip_since = Column(DateTime, nullable=True)
    status = Column(Enum(UserStatus), default=UserStatus.active)
    last_login_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # 关系
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")
    coupons = relationship("UserCoupon", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")


class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    detail = Column(String(255), nullable=False)
    is_default = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="addresses")
    
    __table_args__ = (
        Index('idx_address_user_id', 'user_id'),
    )


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    icon = Column(String(255))
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    
    parent = relationship("Category", remote_side=[id], backref="children")
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    author = Column(String(100))
    publisher = Column(String(100))
    price = Column(DECIMAL(10, 2), nullable=False)
    original_price = Column(DECIMAL(10, 2))
    stock = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"))
    cover_image = Column(String(255))
    images = Column(JSON)
    binding = Column(String(50))
    publish_date = Column(DateTime, nullable=True)
    size_type = Column(Enum(SizeType), default=SizeType.none)
    sizes = Column(JSON)
    size_chart = Column(JSON)
    rating = Column(DECIMAL(2, 1), default=0.0)
    review_count = Column(Integer, default=0)
    sales_count = Column(Integer, default=0)
    status = Column(Enum(ProductStatus), default=ProductStatus.on_sale)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="product", cascade="all, delete-orphan")
    
    __table_args__ = (
        Index('idx_product_category', 'category_id'),
        Index('idx_product_status', 'status'),
        Index('idx_product_price', 'price'),
    )


class CartItem(Base):
    __tablename__ = "cart_items"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    size = Column(String(20), nullable=True)
    quantity = Column(Integer, default=1)
    is_selected = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
    
    __table_args__ = (
        Index('uk_cartitem_user_product_size', 'user_id', 'product_id', 'size', unique=True),
        Index('idx_cartitem_user_id', 'user_id'),
    )


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    order_no = Column(String(50), unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    address_snapshot = Column(JSON, nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    original_amount = Column(DECIMAL(10, 2), nullable=False)
    discount_amount = Column(DECIMAL(10, 2), default=0.00)
    vip_discount = Column(DECIMAL(3, 2), default=1.00)
    coupon_id = Column(Integer, ForeignKey("coupons.id"), nullable=True)
    note = Column(String(500))
    status = Column(Enum(OrderStatus), default=OrderStatus.pending, index=True)
    pay_method = Column(Enum(PayMethod), nullable=True)
    pay_time = Column(DateTime, nullable=True)
    ship_time = Column(DateTime, nullable=True)
    complete_time = Column(DateTime, nullable=True)
    cancel_time = Column(DateTime, nullable=True)
    auto_ship_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), index=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    coupon = relationship("Coupon")
    
    __table_args__ = (
        Index('idx_order_user_id', 'user_id'),
        Index('idx_order_no', 'order_no'),
        Index('idx_order_created_at', 'created_at'),
    )


class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    product_name = Column(String(200), nullable=False)
    product_cover = Column(String(255))
    size = Column(String(20), nullable=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
    
    __table_args__ = (
        Index('idx_orderitem_order_id', 'order_id'),
    )


class Coupon(Base):
    __tablename__ = "coupons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(Enum(CouponType), nullable=False)
    discount_value = Column(DECIMAL(10, 2), nullable=False)
    min_amount = Column(DECIMAL(10, 2), default=0.00)
    max_discount = Column(DECIMAL(10, 2), nullable=True)
    description = Column(String(255))
    total_count = Column(Integer, default=0)
    issued_count = Column(Integer, default=0)
    per_user_limit = Column(Integer, default=1)
    valid_from = Column(DateTime, nullable=False)
    valid_to = Column(DateTime, nullable=False)
    status = Column(Enum(CouponStatus), default=CouponStatus.active, index=True)
    created_at = Column(DateTime, server_default=func.now())
    
    user_coupons = relationship("UserCoupon", back_populates="coupon", cascade="all, delete-orphan")
    
    __table_args__ = (
        Index('idx_coupon_status', 'status'),
        Index('idx_coupon_valid_date', 'valid_from', 'valid_to'),
    )


class UserCoupon(Base):
    __tablename__ = "user_coupons"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    coupon_id = Column(Integer, ForeignKey("coupons.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(UserCouponStatus), default=UserCouponStatus.unused, index=True)
    obtained_at = Column(DateTime, server_default=func.now())
    used_at = Column(DateTime, nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    expires_at = Column(DateTime, nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="coupons")
    coupon = relationship("Coupon", back_populates="user_coupons")
    
    __table_args__ = (
        Index('idx_usercoupon_user_id', 'user_id'),
        Index('idx_usercoupon_status', 'status'),
    )


class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    rating = Column(Integer, nullable=False)
    content = Column(Text)
    images = Column(JSON)
    likes = Column(Integer, default=0)
    is_anonymous = Column(Boolean, default=False)
    status = Column(Enum(ReviewStatus), default=ReviewStatus.approved)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")
    
    __table_args__ = (
        Index('idx_review_product_id', 'product_id'),
        Index('idx_review_user_id', 'user_id'),
        Index('idx_review_rating', 'rating'),
    )


class Favorite(Base):
    __tablename__ = "favorites"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    user = relationship("User", back_populates="favorites")
    product = relationship("Product", back_populates="favorites")
    
    __table_args__ = (
        Index('idx_favorite_user_id', 'user_id'),
        Index('uk_favorite_user_product', 'user_id', 'product_id', unique=True),
    )
