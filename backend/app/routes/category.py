from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models import Category, Product, User
from app.schemas import CategoryCreate, CategoryResponse, ProductResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/categories", tags=["分类"])


@router.get("", response_model=List[CategoryResponse])
async def get_categories(
    parent_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Category).filter(Category.is_active == True)
    
    if parent_id is not None:
        query = query.filter(Category.parent_id == parent_id)
    else:
        query = query.filter(Category.parent_id == None)
    
    categories = query.order_by(Category.sort_order).all()
    return categories


@router.get("/tree", response_model=List[CategoryResponse])
async def get_category_tree(db: Session = Depends(get_db)):
    # 获取所有一级分类
    root_categories = db.query(Category).filter(
        Category.is_active == True,
        Category.parent_id == None
    ).order_by(Category.sort_order).all()
    
    def build_tree(category: Category) -> dict:
        result = CategoryResponse.model_validate(category)
        if category.children:
            result.children = [build_tree(child) for child in category.children if child.is_active]
        return result
    
    return [build_tree(cat) for cat in root_categories]


@router.post("", response_model=CategoryResponse)
async def create_category(
    category_data: CategoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # 检查父分类是否存在
    if category_data.parent_id:
        parent = db.query(Category).filter(Category.id == category_data.parent_id).first()
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="父分类不存在"
            )
    
    db_category = Category(**category_data.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    
    return db_category
