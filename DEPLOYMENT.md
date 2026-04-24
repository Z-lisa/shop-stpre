# 书店商城 - 完整项目部署指南

## 项目概述

这是一个完整的书店商城项目，包含前后端：
- **后端**: Python FastAPI + MySQL
- **前端**: Vue 3 + Vite + Pinia
- **功能**: 用户认证、商品管理、购物车、订单、优惠券、评价等

---

## 环境要求

### 后端
- Python 3.9+
- MySQL 8.0+
- pip 或 poetry

### 前端
- Node.js 16+
- npm 或 yarn

---

## 快速开始

### 1. 数据库配置

#### 安装 MySQL
确保已安装 MySQL 8.0+，并创建数据库用户：

```sql
-- 登录 MySQL
mysql -u root -p

-- 创建数据库和用户（可选，也可以使用 root）
CREATE DATABASE book_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. 后端部署

#### 步骤 1: 进入后端目录
```bash
cd backend
```

#### 步骤 2: 安装依赖
```bash
# 方式 1: 使用 pip
pip install -r requirements.txt

# 方式 2: 使用 poetry（推荐）
poetry install
```

#### 步骤 3: 配置环境变量
编辑 `backend/.env` 文件：
```env
DATABASE_URL=mysql+pymysql://root:你的密码@localhost:3306/book_shop?charset=utf8mb4
JWT_SECRET_KEY=修改为一个随机密钥
```

#### 步骤 4: 初始化数据库
```bash
python init_db.py
```

这会：
- 创建数据库表
- 插入初始分类数据
- 插入示例商品
- 插入优惠券数据

#### 步骤 5: 启动后端服务
```bash
# 方式 1: 使用 uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 方式 2: 直接运行
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000 查看 API 文档
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

### 3. 前端部署

#### 步骤 1: 进入项目根目录
```bash
cd c:\Users\EDY\Desktop\book-shop
```

#### 步骤 2: 安装依赖
```bash
npm install
```

#### 步骤 3: 配置环境变量
`.env` 文件已创建，默认配置：
```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

#### 步骤 4: 启动开发服务器
```bash
npm run dev
```

访问 http://localhost:5173

---

## 测试账号

后端已创建示例数据，但需要手动注册账号。

### 注册流程
1. 访问 http://localhost:5173/login
2. 点击"注册"
3. 输入用户名、密码等信息
4. 注册成功后自动登录

---

## API 接口文档

启动后端后访问：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 主要接口

#### 认证
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录
- `GET /api/v1/auth/me` - 获取当前用户信息

#### 商品
- `GET /api/v1/products` - 获取商品列表
- `GET /api/v1/products/{id}` - 获取商品详情
- `GET /api/v1/categories` - 获取分类列表

#### 购物车
- `GET /api/v1/cart` - 获取购物车
- `POST /api/v1/cart/items` - 添加到购物车
- `PUT /api/v1/cart/items/{id}` - 更新购物车
- `DELETE /api/v1/cart/items/{id}` - 删除购物车商品

#### 订单
- `GET /api/v1/orders` - 获取订单列表
- `POST /api/v1/orders` - 创建订单
- `POST /api/v1/orders/{id}/pay` - 支付订单
- `POST /api/v1/orders/{id}/cancel` - 取消订单

#### 地址
- `GET /api/v1/addresses` - 获取地址列表
- `POST /api/v1/addresses` - 新增地址
- `PUT /api/v1/addresses/{id}` - 更新地址
- `DELETE /api/v1/addresses/{id}` - 删除地址

#### 优惠券
- `GET /api/v1/coupons` - 获取优惠券列表
- `POST /api/v1/coupons/{id}/claim` - 领取优惠券
- `GET /api/v1/coupons/my` - 我的优惠券

---

## 项目结构

### 后端
```
backend/
├── app/
│   ├── config.py          # 配置
│   ├── database.py        # 数据库连接
│   ├── models.py          # 数据模型
│   ├── schemas.py         # Pydantic 模型
│   ├── security.py        # 安全工具（JWT、密码加密）
│   ├── dependencies.py    # 依赖注入
│   ├── main.py            # FastAPI 应用入口
│   └── routes/            # 路由模块
│       ├── auth.py
│       ├── user.py
│       ├── address.py
│       ├── category.py
│       ├── product.py
│       ├── cart.py
│       ├── order.py
│       ├── coupon.py
│       ├── review.py
│       └── favorite.py
├── init_db.py             # 数据库初始化脚本
├── requirements.txt       # Python 依赖
└── .env                   # 环境变量
```

### 前端
```
src/
├── api/                   # API 封装
│   ├── request.js        # Axios 配置
│   ├── auth.js
│   ├── product.js
│   ├── cart.js
│   ├── order.js
│   ├── address.js
│   ├── coupon.js
│   ├── review.js
│   └── favorite.js
├── stores/                # Pinia 状态管理
│   ├── user.js
│   ├── cart.js
│   ├── order.js
│   ├── address.js
│   └── coupon.js
├── views/                 # 页面组件
├── components/            # 公共组件
└── router/                # 路由配置
```

---

## 常见问题

### 1. 后端启动失败

**问题**: `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server")`

**解决**: 
- 检查 MySQL 服务是否启动
- 检查 `.env` 中的数据库连接配置
- 确认数据库用户权限

### 2. 前端无法连接后端

**问题**: `Network Error`

**解决**:
- 确认后端服务已启动（http://localhost:8000）
- 检查 `.env` 中的 `VITE_API_BASE_URL` 配置
- 检查浏览器控制台 CORS 错误

### 3. 数据库初始化失败

**问题**: `Table doesn't exist`

**解决**:
```bash
# 重新运行初始化脚本
cd backend
python init_db.py
```

### 4. 登录失败

**问题**: `401 Unauthorized`

**解决**:
- 确认已注册账号
- 检查用户名密码是否正确
- 查看后端日志确认错误信息

---

## 开发说明

### 后端开发

#### 添加新路由
1. 在 `app/routes/` 创建新的路由文件
2. 在 `app/main.py` 中注册路由

#### 添加新模型
1. 在 `app/models.py` 定义 SQLAlchemy 模型
2. 在 `app/schemas.py` 定义 Pydantic 模型
3. 运行数据库迁移或重新初始化

### 前端开发

#### 添加新 API
1. 在 `src/api/` 创建对应的 API 文件
2. 在对应的 store 中调用 API

#### 添加新页面
1. 在 `src/views/` 创建页面组件
2. 在 `src/router/index.js` 配置路由

---

## 生产部署

### 后端部署

#### 使用 Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

#### 使用 Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 前端部署

#### 构建
```bash
npm run build
```

#### 使用 Nginx
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/dist;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 下一步功能

当前项目已实现基础电商功能，后续可以添加：

1. **支付集成**
   - 微信支付
   - 支付宝支付

2. **物流跟踪**
   - 对接快递 API
   - 实时物流信息

3. **消息通知**
   - 邮件通知
   - 短信通知
   - 站内消息

4. **数据分析**
   - 销售统计
   - 用户行为分析

5. **管理后台**
   - 商品管理
   - 订单管理
   - 用户管理

---

## 技术支持

如有问题，请检查：
1. 后端日志
2. 前端浏览器控制台
3. 数据库连接状态
4. API 文档确认接口参数

---

**祝部署顺利！** 🎉
