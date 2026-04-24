@echo off
chcp 65001 >nul
echo ========================================
echo     书店商城 - 快速启动脚本
echo ========================================
echo.

REM 检查 Python
echo [1/4] 检查 Python 环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未找到 Python，请先安装 Python 3.9+
    pause
    exit /b 1
)
echo ✓ Python 环境正常

REM 检查 MySQL
echo [2/4] 检查 MySQL 连接...
python -c "import pymysql; pymysql.connect(host='localhost', user='root', password='root')" >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：无法连接 MySQL，请检查：
echo    1. MySQL 服务是否启动
echo    2. 用户名密码是否正确 (backend/.env)
    pause
    exit /b 1
)
echo ✓ MySQL 连接正常

REM 初始化数据库
echo [3/4] 初始化数据库...
cd backend
if not exist app\__init__.py (
    type nul > app\__init__.py
)
if not exist app\routes\__init__.py (
    type nul > app\routes\__init__.py
)
python init_db.py
if errorlevel 1 (
    echo ❌ 数据库初始化失败
    pause
    exit /b 1
)
echo ✓ 数据库初始化完成

REM 启动后端
echo [4/4] 启动后端服务...
echo.
echo ========================================
echo  后端服务已启动
echo  访问地址：http://localhost:8000
echo  API 文档：http://localhost:8000/docs
echo ========================================
echo.
echo 按 Ctrl+C 停止服务
echo.

start http://localhost:8000/docs
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
