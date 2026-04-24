from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.routes import auth, user, address, category, product, cart, order, coupon, review, favorite

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="书店商城 API",
    description="书店商城后端 API 接口",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(address.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
app.include_router(product.router, prefix="/api/v1")
app.include_router(cart.router, prefix="/api/v1")
app.include_router(order.router, prefix="/api/v1")
app.include_router(coupon.router, prefix="/api/v1")
app.include_router(review.router, prefix="/api/v1")
app.include_router(favorite.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": "书店商城 API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
