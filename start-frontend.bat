@echo off
chcp 65001 >nul
echo ========================================
echo     书店商城 - 前端启动脚本
echo ========================================
echo.

echo [1/2] 检查 Node.js 环境...
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未找到 Node.js，请先安装 Node.js 16+
    pause
    exit /b 1
)
echo ✓ Node.js 环境正常

echo [2/2] 检查依赖...
if not exist node_modules (
    echo 正在安装依赖，请稍候...
    call npm install
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
)
echo ✓ 依赖安装完成

echo.
echo ========================================
echo  启动前端开发服务器...
echo ========================================
echo.

start http://localhost:5173
call npm run dev
