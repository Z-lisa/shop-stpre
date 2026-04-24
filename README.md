# 📚 书店商城 - 完整电商平台

> 基于 Vue 3 + FastAPI 的全栈电商平台

![Vue 3](https://img.shields.io/badge/Vue-3.4.0-4FC08D?logo=vue.js)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql)

---

## ✨ 特性

### 前端特性
- 🎨 **现代化 UI** - 基于 TailwindCSS 的清新设计
- 📱 **响应式布局** - 完美适配移动端
- 🛒 **完整购物流程** - 浏览、加购、结算、支付
- 👤 **用户系统** - 注册登录、VIP 会员体系
- 🎫 **优惠券系统** - 领取、使用优惠券
- ⭐ **评价系统** - 商品评价、星级评分
- ❤️ **收藏功能** - 商品收藏管理
- 📍 **地址管理** - 多地址管理、默认地址

### 后端特性
- 🔐 **JWT 认证** - 安全的身份验证
- 📊 **RESTful API** - 规范的接口设计
- 🗄 **MySQL 数据库** - 稳定的数据存储
- 🔒 **密码加密** - bcrypt 加密存储
- 🚀 **高性能** - FastAPI 异步处理
- 📝 **API 文档** - 自动生成 Swagger 文档

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.9+
- **Node.js**: 16+
- **MySQL**: 8.0+

### 一键启动

#### Windows 用户

1. **启动后端**
   ```bash
   双击运行：start-backend.bat
   ```

2. **启动前端**
   ```bash
   双击运行：start-frontend.bat
   ```

#### 手动启动

**后端:**
```bash
cd backend
pip install -r requirements.txt
python init_db.py
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**前端:**
```bash
npm install
npm run dev
```

---

## 📦 项目结构

```
book-shop/
├── backend/                    # 后端项目
│   ├── app/
│   │   ├── config.py          # 配置
│   │   ├── database.py        # 数据库连接
│   │   ├── models.py          # 数据模型
│   │   ├── schemas.py         # Pydantic 模型
│   │   ├── security.py        # 安全工具
│   │   ├── dependencies.py    # 依赖注入
│   │   ├── main.py            # 应用入口
│   │   └── routes/            # 路由模块
│   │       ├── auth.py        # 认证
│   │       ├── user.py        # 用户
│   │       ├── address.py     # 地址
│   │       ├── category.py    # 分类
│   │       ├── product.py     # 商品
│   │       ├── cart.py        # 购物车
│   │       ├── order.py       # 订单
│   │       ├── coupon.py      # 优惠券
│   │       ├── review.py      # 评价
│   │       └── favorite.py    # 收藏
│   ├── init_db.py             # 数据库初始化
│   ├── requirements.txt       # Python 依赖
│   └── .env                   # 环境变量
│
├── src/                        # 前端源码
│   ├── api/                   # API 封装
│   │   ├── request.js        # Axios 配置
│   │   ├── auth.js
│   │   ├── product.js
│   │   ├── cart.js
│   │   ├── order.js
│   │   ├── address.js
│   │   ├── coupon.js
│   │   ├── review.js
│   │   └── favorite.js
│   ├── stores/                # Pinia 状态管理
│   │   ├── user.js
│   │   ├── cart.js
│   │   ├── order.js
│   │   ├── address.js
│   │   └── coupon.js
│   ├── views/                 # 页面组件
│   ├── components/            # 公共组件
│   └── router/                # 路由配置
│
├── start-backend.bat          # 后端启动脚本
├── start-frontend.bat         # 前端启动脚本
└── DEPLOYMENT.md              # 部署文档
```

---

## 🛠 技术栈

### 前端
- **框架**: Vue 3 (Composition API)
- **构建工具**: Vite
- **状态管理**: Pinia
- **路由**: Vue Router
- **HTTP 客户端**: Axios
- **UI 框架**: TailwindCSS

### 后端
- **框架**: FastAPI
- **ORM**: SQLAlchemy
- **数据库**: MySQL 8.0+
- **认证**: JWT (python-jose)
- **加密**: bcrypt (passlib)
- **验证**: Pydantic

---

## 📖 API 文档

启动后端后访问：
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 核心接口

#### 认证模块
```
POST   /api/v1/auth/register      用户注册
POST   /api/v1/auth/login         用户登录
GET    /api/v1/auth/me            获取当前用户
PUT    /api/v1/auth/me            更新用户信息
POST   /api/v1/auth/change-password  修改密码
```

#### 商品模块
```
GET    /api/v1/products           获取商品列表
GET    /api/v1/products/{id}      获取商品详情
GET    /api/v1/products/{id}/recommend  推荐商品
GET    /api/v1/categories         获取分类列表
GET    /api/v1/categories/tree    获取分类树
```

#### 购物车模块
```
GET    /api/v1/cart               获取购物车
POST   /api/v1/cart/items         添加到购物车
PUT    /api/v1/cart/items/{id}    更新购物车
DELETE /api/v1/cart/items/{id}    删除商品
POST   /api/v1/cart/select/{id}   切换选中
POST   /api/v1/cart/select-all    全选
```

#### 订单模块
```
GET    /api/v1/orders             获取订单列表
POST   /api/v1/orders             创建订单
GET    /api/v1/orders/{id}        订单详情
POST   /api/v1/orders/{id}/pay    支付订单
POST   /api/v1/orders/{id}/cancel 取消订单
POST   /api/v1/orders/{id}/confirm 确认收货
```

#### 地址模块
```
GET    /api/v1/addresses          获取地址列表
POST   /api/v1/addresses          新增地址
PUT    /api/v1/addresses/{id}     更新地址
DELETE /api/v1/addresses/{id}     删除地址
PUT    /api/v1/addresses/{id}/default 设为默认
```

#### 优惠券模块
```
GET    /api/v1/coupons            获取优惠券列表
POST   /api/v1/coupons/{id}/claim 领取优惠券
GET    /api/v1/coupons/my         我的优惠券
GET    /api/v1/coupons/available  可用优惠券
```

---

## 💾 数据库设计

### 核心表

- **users** - 用户表
- **addresses** - 地址表
- **categories** - 分类表
- **products** - 商品表
- **cart_items** - 购物车表
- **orders** - 订单表
- **order_items** - 订单商品表
- **coupons** - 优惠券表
- **user_coupons** - 用户优惠券表
- **reviews** - 评价表
- **favorites** - 收藏表

详细表结构请查看 `backend/app/models.py`

---

## 🎯 功能清单

### 已实现功能

✅ **用户系统**
- [x] 用户注册/登录
- [x] JWT  Token 认证
- [x] VIP 会员体系（消费满 500 自动升级）
- [x] 会员折扣（85 折）

✅ **商品系统**
- [x] 商品列表/详情
- [x] 商品分类
- [x] 商品搜索
- [x] 多规格商品（尺码选择）
- [x] 商品推荐
- [x] 商品评价

✅ **购物系统**
- [x] 购物车管理
- [x] 商品加减
- [x] 数量调整
- [x] 全选/单选
- [x] 库存检查

✅ **订单系统**
- [x] 订单创建
- [x] 订单列表/详情
- [x] 订单状态管理
- [x] 自动发货（5 分钟）
- [x] 订单取消
- [x] 确认收货

✅ **营销系统**
- [x] 优惠券领取
- [x] 优惠券使用
- [x] 满减券/折扣券
- [x] 自动计算最优折扣

✅ **地址管理**
- [x] 地址 CRUD
- [x] 默认地址
- [x] 地址选择

✅ **收藏系统**
- [x] 商品收藏
- [x] 收藏列表

---

## 🔧 配置说明

### 后端配置 (.env)

```env
# 数据库
DATABASE_URL=mysql+pymysql://root:密码@localhost:3306/book_shop?charset=utf8mb4

# JWT
JWT_SECRET_KEY=你的密钥
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:5173"]
```

### 前端配置 (.env)

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

---

## 🐛 常见问题

### 1. 后端无法连接数据库

**解决**:
- 检查 MySQL 服务是否启动
- 确认 `.env` 中的数据库配置正确
- 检查数据库用户权限

### 2. 前端请求失败（CORS 错误）

**解决**:
- 确认后端已启动
- 检查后端 `.env` 中的 `BACKEND_CORS_ORIGINS`
- 确认前端 `.env` 的 API 地址正确

### 3. 登录失败

**解决**:
- 先注册账号
- 检查用户名密码
- 查看后端日志

### 4. 数据库表不存在

**解决**:
```bash
cd backend
python init_db.py
```

---

## 📝 开发指南

### 添加新 API

1. 在 `backend/app/routes/` 创建路由文件
2. 在 `backend/app/main.py` 注册路由
3. 在 `src/api/` 创建前端 API 封装
4. 在对应 store 中调用

### 添加新页面

1. 在 `src/views/` 创建页面组件
2. 在 `src/router/index.js` 配置路由
3. 调用 API 获取数据

---

## 🚀 生产部署

详见 [DEPLOYMENT.md](./DEPLOYMENT.md)

---

## 📄 开源协议

MIT License

---

## 🙏 致谢

感谢以下开源项目：

- [Vue.js](https://vuejs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [Pinia](https://pinia.vuejs.org/)

---

**Happy Coding!** 🎉
