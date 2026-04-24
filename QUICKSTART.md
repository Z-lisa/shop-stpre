# 🚀 快速开始指南

## 第一次运行？按这个步骤操作！

### 步骤 1: 检查环境

#### 1. 检查 Python
打开命令行，输入：
```bash
python --version
```
应该显示 `Python 3.9.x` 或更高版本

#### 2. 检查 MySQL
```bash
# Windows
mysql --version

# 或检查服务是否运行
net start | findstr MySQL
```

如果未安装 MySQL，请前往 https://dev.mysql.com/downloads/mysql/ 下载安装

#### 3. 检查 Node.js
```bash
node --version
npm --version
```
应该显示 `v16.x.x` 或更高版本

---

### 步骤 2: 配置数据库

#### 方式 1: 使用现有 MySQL

编辑 `backend/.env` 文件，修改数据库配置：
```env
DATABASE_URL=mysql+pymysql://root:你的密码@localhost:3306/book_shop?charset=utf8mb4
```

#### 方式 2: 创建新数据库用户（推荐）

登录 MySQL:
```sql
mysql -u root -p
```

执行 SQL:
```sql
-- 创建数据库
CREATE DATABASE book_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建用户（可选）
CREATE USER 'bookshop'@'localhost' IDENTIFIED BY 'bookshop123';
GRANT ALL PRIVILEGES ON book_shop.* TO 'bookshop'@'localhost';
FLUSH PRIVILEGES;
```

然后更新 `backend/.env`:
```env
DATABASE_URL=mysql+pymysql://bookshop:bookshop123@localhost:3306/book_shop?charset=utf8mb4
```

---

### 步骤 3: 启动后端

#### Windows 用户（推荐）
直接双击运行：
```
start-backend.bat
```

#### 手动启动
```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 初始化数据库（仅第一次）
python init_db.py

# 启动服务
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ 成功标志：
- 看到 `Uvicorn running on http://0.0.0.0:8000`
- 浏览器访问 http://localhost:8000/docs 能看到 API 文档

---

### 步骤 4: 启动前端

#### Windows 用户（推荐）
直接双击运行：
```
start-frontend.bat
```

#### 手动启动
```bash
# 安装依赖（仅第一次）
npm install

# 启动开发服务器
npm run dev
```

✅ 成功标志：
- 看到 `Local: http://localhost:5173/`
- 浏览器自动打开 http://localhost:5173

---

### 步骤 5: 注册账号

1. 访问 http://localhost:5173
2. 点击"登录"
3. 点击"注册账号"
4. 填写信息：
   - 用户名：test
   - 密码：123456
   - 确认密码：123456
5. 点击注册

---

### 步骤 6: 开始购物

✅ 现在你可以：
- 🛍 浏览商品（图书、服装、鞋子）
- 🛒 添加商品到购物车
- 📝 创建订单
- 🎫 领取和使用优惠券
- ⭐ 发布评价
- ❤️ 收藏商品
- 📍 管理收货地址

---

## 🐛 遇到问题？

### 问题 1: 后端启动失败 - 数据库连接错误

**错误信息**: `Can't connect to MySQL server`

**解决方案**:
1. 检查 MySQL 服务是否启动
   ```bash
   # Windows
   net start MySQL80
   
   # 或在服务管理器中启动
   services.msc
   ```

2. 确认 `backend/.env` 中的数据库配置正确
   ```env
   DATABASE_URL=mysql+pymysql://root:正确密码@localhost:3306/book_shop?charset=utf8mb4
   ```

3. 测试连接
   ```bash
   python -c "import pymysql; pymysql.connect(host='localhost', user='root', password='你的密码')"
   ```

---

### 问题 2: 前端无法连接后端

**错误信息**: `Network Error` 或 CORS 错误

**解决方案**:
1. 确认后端已启动（访问 http://localhost:8000）
2. 检查 `backend/.env` 中的 CORS 配置
   ```env
   BACKEND_CORS_ORIGINS=["http://localhost:5173","http://localhost:5174"]
   ```
3. 确认前端 `.env` 配置正确
   ```env
   VITE_API_BASE_URL=http://localhost:8000/api/v1
   ```

---

### 问题 3: 数据库初始化失败

**错误信息**: `Table doesn't exist`

**解决方案**:
```bash
cd backend
python init_db.py
```

如果还有问题，删除数据库重新创建：
```sql
DROP DATABASE IF EXISTS book_shop;
CREATE DATABASE book_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

然后重新运行初始化脚本。

---

### 问题 4: npm install 失败

**错误信息**: 各种 npm 错误

**解决方案**:
1. 清除 npm 缓存
   ```bash
   npm cache clean --force
   ```

2. 使用淘宝镜像
   ```bash
   npm config set registry https://registry.npmmirror.com
   npm install
   ```

3. 删除 node_modules 重新安装
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

---

### 问题 5: Python 依赖安装失败

**错误信息**: `Could not find a version that satisfies the requirement`

**解决方案**:
1. 升级 pip
   ```bash
   python -m pip install --upgrade pip
   ```

2. 使用国内镜像
   ```bash
   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

3. 检查 Python 版本（需要 3.9+）
   ```bash
   python --version
   ```

---

## 📝 测试数据

初始化脚本会自动创建以下数据：

### 商品分类
- 文学小说
- 历史传记
- 科技图书
- 生活休闲
- 服装
- 鞋子

### 示例商品
- 《活着》- 余华
- 《百年孤独》- 马尔克斯
- 《Python 编程》- Eric Matthes
- 春季新款 T 恤（多尺码）
- 运动鞋（多尺码）

### 优惠券
- 新人优惠券（满 100 减 20）
- 满减券（满 300 减 50）
- 折扣券（9 折，最高减 100）

---

## 🎯 下一步

完成上述步骤后，你可以：

1. **浏览商品** - 查看各个分类的商品
2. **添加到购物车** - 选择商品和数量
3. **创建订单** - 选择地址、使用优惠券
4. **模拟支付** - 体验完整购物流程
5. **发布评价** - 对已完成订单评价

---

## 📚 更多文档

- [完整部署文档](./DEPLOYMENT.md)
- [API 文档](http://localhost:8000/docs)
- [项目说明](./README.md)

---

**祝你使用愉快！** 🎉

如有问题，请查看日志：
- 后端日志：命令行输出
- 前端日志：浏览器控制台（F12）
