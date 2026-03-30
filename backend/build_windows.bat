@echo off
chcp 65001 >nul
echo 🚀 开始进行 Windows 打包...
echo.

:: 1. 尝试自动激活本目录下的虚拟环境
if exist venv\Scripts\activate.bat (
    echo [1/3] 检测到本地环境，正在自动激活 (venv)...
    call venv\Scripts\activate.bat
) else (
    echo [1/3] 警告: 未找到 backend/venv 虚拟环境！如果你装在别的地方，请手动激活。
)

:: 2. 检查安装
echo.
echo [2/3] 检查并安装打包必备工具：PyInstaller...
pip install pyinstaller

echo.
echo [3/3] 开始执行核心编译逻辑...
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist

:: 许多人在打包 FastAPI 项目后闪退，通常是底层 uvicorn/tortoise 相关的动态库在打包阶段丢失。
:: 所以下面这一长串 --hidden-import 就是用来彻底根治闪退问题的。
pyinstaller --name "年会抽奖系统" --noconfirm --onedir --add-data "static;static" --hidden-import="app.models" --hidden-import="aerich.models" --hidden-import="aiosqlite" --hidden-import="tortoise.backends.sqlite" --hidden-import="pydantic.v1" --hidden-import="uvicorn.logging" --hidden-import="uvicorn.loops" --hidden-import="uvicorn.loops.auto" --hidden-import="uvicorn.protocols" --hidden-import="uvicorn.protocols.http" --hidden-import="uvicorn.protocols.http.auto" --hidden-import="uvicorn.protocols.websockets" --hidden-import="uvicorn.protocols.websockets.auto" --hidden-import="uvicorn.lifespan" --hidden-import="uvicorn.lifespan.on" app/main.py

echo.
echo 🎉 打包完成！
echo 👉 你的无木马绿色版交付程序在【dist\年会抽奖系统】文件夹里。
echo.
echo 【最后记得】：
echo 去 dist\年会抽奖系统 里手动复制一份 .env 放进去。
echo.
pause
