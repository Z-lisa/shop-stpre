# 购物商城 - 项目启动说明

## 环境要求
- Node.js >= 14.0.0
- npm >= 6.0.0

## 安装步骤

### 1. 安装 Node.js
如果尚未安装 Node.js，请访问 [Node.js 官网](https://nodejs.org/) 下载安装，或使用以下方式：

```bash
# 使用 Homebrew (macOS)
brew install node

# 或使用 nvm (推荐)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install node
```

### 2. 安装项目依赖
```bash
cd /Users/echo/Desktop/项目/shop
npm install
```

### 3. 启动开发服务器
```bash
npm run dev
```

启动成功后，访问 http://localhost:3000

### 4. 构建生产版本
```bash
npm run build
```

## 项目结构
```
book-mall/
├── src/
│   ├── views/          # 页面组件
│   │   ├── Home.vue         # 首页
│   │   ├── Category.vue     # 分类页
│   │   ├── Cart.vue         # 购物车
│   │   ├── Profile.vue      # 个人中心
│   │   ├── BookDetail.vue   # 购物详情
│   │   ├── Search.vue       # 搜索结果
│   │   ├── Checkout.vue     # 结算页
│   │   └── OrderSuccess.vue # 订单成功
│   ├── stores/         # Pinia 状态管理
│   │   ├── cart.js          # 购物车状态
│   │   └── favorites.js     # 收藏状态
│   ├── data/           # 本地模拟数据
│   │   └── books.js         # 购物数据(42本)
│   ├── router/         # 路由配置
│   │   └── index.js
│   ├── App.vue         # 根组件
│   ├── main.js         # 入口文件
│   └── style.css       # 全局样式
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
└── postcss.config.js
```

## 功能特性
- ✅ 8个核心页面（首页、分类、购物车、个人中心、购物详情、搜索、结算、订单成功）
- ✅ 42本购物数据，8大分类
- ✅ 搜索功能（支持书名/作者搜索）
- ✅ 购物车功能（增删改查、全选、计算总价）
- ✅ 收藏功能
- ✅ 响应式移动端适配
- ✅ 本地存储数据持久化




