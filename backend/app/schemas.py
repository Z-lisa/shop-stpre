from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from enum import Enum


# ============ 用户相关 ============

class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    nickname: Optional[str] = Field(None, max_length=50)
    gender: Optional[GenderEnum] = None


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    gender: Optional[GenderEnum] = None
    avatar: Optional[str] = None


class UserResponse(UserBase):
    id: int
    avatar: Optional[str] = None
    total_spent: float = 0.0
    is_vip: bool = False
    vip_since: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# ============ 地址相关 ============

class AddressBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    phone: str = Field(..., min_length=11, max_length=20)
    province: str
    city: str
    district: str
    detail: str = Field(..., min_length=1, max_length=255)


class AddressCreate(AddressBase):
    is_default: bool = False


class AddressUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    detail: Optional[str] = None
    is_default: Optional[bool] = None


class AddressResponse(AddressBase):
    id: int
    user_id: int
    is_default: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============ 分类相关 ============

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    icon: Optional[str] = None
    sort_order: int = 0


class CategoryCreate(CategoryBase):
    parent_id: Optional[int] = None


class CategoryResponse(CategoryBase):
    id: int
    parent_id: Optional[int] = None
    is_active: bool
    created_at: datetime
    children: List['CategoryResponse'] = []
    
    model_config = ConfigDict(from_attributes=True)


# ============ 商品相关 ============

class SizeTypeEnum(str, Enum):
    none = "none"
    clothing = "clothing"
    shoes = "shoes"


class ProductStatusEnum(str, Enum):
    on_sale = "on_sale"
    off_sale = "off_sale"
    out_of_stock = "out_of_stock"


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    price: float = Field(..., gt=0)
    original_price: Optional[float] = None
    stock: int = Field(default=0, ge=0)
    category_id: Optional[int] = None
    cover_image: Optional[str] = None
    images: Optional[list] = None
    binding: Optional[str] = None
    publish_date: Optional[datetime] = None
    size_type: SizeTypeEnum = SizeTypeEnum.none
    sizes: Optional[list] = None
    size_chart: Optional[list] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    original_price: Optional[float] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None
    cover_image: Optional[str] = None
    images: Optional[list] = None
    status: Optional[ProductStatusEnum] = None


class ProductResponse(ProductBase):
    id: int
    rating: float = 0.0
    review_count: int = 0
    sales_count: int = 0
    status: ProductStatusEnum
    created_at: datetime
    updated_at: datetime
    category: Optional[CategoryResponse] = None
    
    model_config = ConfigDict(from_attributes=True)


# ============ 购物车相关 ============

class CartItemBase(BaseModel):
    product_id: int
    size: Optional[str] = None
    quantity: int = Field(default=1, ge=1, le=99)


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: Optional[int] = Field(None, ge=1, le=99)
    is_selected: Optional[bool] = None


class ProductSimple(BaseModel):
    id: int
    name: str
    author: Optional[str]
    price: float
    cover_image: Optional[str]
    stock: int
    size_type: SizeTypeEnum
    sizes: Optional[list] = None
    
    model_config = ConfigDict(from_attributes=True)


class CartItemResponse(BaseModel):
    id: int
    product: ProductSimple
    size: Optional[str]
    quantity: int
    is_selected: bool
    
    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    items: List[CartItemResponse]
    total_items: int
    total_price: float


# ============ 订单相关 ============

class OrderStatusEnum(str, Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    completed = "completed"
    cancelled = "cancelled"


class PayMethodEnum(str, Enum):
    wechat = "wechat"
    alipay = "alipay"
    balance = "balance"


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    size: Optional[str] = None


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    address_id: int
    coupon_id: Optional[int] = None
    note: Optional[str] = None


class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    product_cover: Optional[str]
    size: Optional[str]
    quantity: int
    unit_price: float
    subtotal: float
    
    model_config = ConfigDict(from_attributes=True)


class AddressSnapshot(BaseModel):
    name: str
    phone: str
    province: str
    city: str
    district: str
    detail: str


class OrderResponse(BaseModel):
    id: int
    order_no: str
    user_id: int
    address_snapshot: AddressSnapshot
    total_amount: float
    original_amount: float
    discount_amount: float
    vip_discount: float
    note: Optional[str]
    status: OrderStatusEnum
    pay_method: Optional[PayMethodEnum]
    pay_time: Optional[datetime]
    ship_time: Optional[datetime]
    complete_time: Optional[datetime]
    created_at: datetime
    items: List[OrderItemResponse]
    
    model_config = ConfigDict(from_attributes=True)


# ============ 优惠券相关 ============

class CouponTypeEnum(str, Enum):
    fixed = "fixed"
    percentage = "percentage"


class CouponStatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    exhausted = "exhausted"


class CouponBase(BaseModel):
    name: str
    type: CouponTypeEnum
    discount_value: float
    min_amount: float = 0
    max_discount: Optional[float] = None
    description: Optional[str] = None


class CouponCreate(CouponBase):
    total_count: int = 0
    per_user_limit: int = 1
    valid_from: datetime
    valid_to: datetime


class CouponResponse(CouponBase):
    id: int
    status: CouponStatusEnum
    valid_from: datetime
    valid_to: datetime
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class UserCouponStatusEnum(str, Enum):
    unused = "unused"
    used = "used"
    expired = "expired"


class UserCouponResponse(BaseModel):
    id: int
    coupon: CouponResponse
    status: UserCouponStatusEnum
    obtained_at: datetime
    expires_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============ 评价相关 ============

class ReviewBase(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    content: Optional[str] = None
    images: Optional[list] = None
    is_anonymous: bool = False


class ReviewCreate(ReviewBase):
    product_id: int
    order_id: Optional[int] = None


class ReviewUpdate(BaseModel):
    content: Optional[str] = None
    images: Optional[list] = None


class UserSimple(BaseModel):
    id: int
    username: str
    nickname: Optional[str]
    avatar: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)


class ReviewResponse(ReviewBase):
    id: int
    user: Optional[UserSimple]
    product_id: int
    likes: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============ 收藏相关 ============

class FavoriteCreate(BaseModel):
    product_id: int


class FavoriteResponse(BaseModel):
    id: int
    product: ProductSimple
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============ 通用响应 ============

class ResponseModel(BaseModel):
    code: int = 200
    message: str = "success"
    data: Optional[dict] = None


class PaginatedResponse(BaseModel):
    list: List[dict]
    pagination: dict


class ErrorResponse(BaseModel):
    code: int
    message: str
    errors: Optional[List[dict]] = None
