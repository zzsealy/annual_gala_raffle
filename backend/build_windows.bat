@echo off
chcp 65001 >nul
echo 🚀 开始进行 Windows 打包...
echo 1. 确保你已经在虚拟环境中安装了所需依赖 (pip install -r requirements.txt)
echo 2. 检查并安装 PyInstaller 工具
pip install pyinstaller

echo.
echo 3. 开始执行核心打包逻辑...
:: 清理过去的残留编译文件
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist

:: 核心打包命令
:: --name: 最终生成的 exe 名字
:: --noconfirm: 不需询问，直接覆盖上次产出
:: --onedir: 推荐模式，生成文件夹而不是单体exe（单体exe解压极慢且容易被杀毒软件误杀）
:: --add-data "static;static": 将你编译好的炫酷前端挂载到_MEIPASS虚拟目录
:: --hidden-import: 防止 Tortoise ORM 动态加载的模块以及 SQLite 驱动在打包时丢失
pyinstaller --name "年会抽奖系统" --noconfirm --onedir --add-data "static;static" --hidden-import="app.models" --hidden-import="aiosqlite" --hidden-import="tortoise.backends.sqlite" --hidden-import="pydantic.v1" app/main.py

echo.
echo 🎉 打包完成！
echo 👉 你的交付程序在【dist\年会抽奖系统】文件夹里。
echo.
echo 【最后重要操作提醒，发给领导前必做】：
echo 1. 去 dist\年会抽奖系统 文件夹里，手动新建一个名叫 data 文件夹。
echo 2. 把你的 .env 文件复制进 dist\年会抽奖系统 文件夹（放在 exe 旁边）。
echo 3. 把你要抽奖的名单 person.xlsx 也可以复制进去。
echo.
pause
