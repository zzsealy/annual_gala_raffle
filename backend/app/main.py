import os
import sys
import traceback

try:
    import time
    import threading
    import webbrowser
    import pandas as pd
    from fastapi import FastAPI
    from tortoise.contrib.fastapi import register_tortoise
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse, HTMLResponse
    from app.db import TORTOISE_ORM, BASE_DIR
    from app.api import router as api_router
    from app.models import Participant, ParticipantSpecial
    from app.participant_import import (
        build_participants_from_excel,
        build_special_participants_from_excel,
    )
except Exception as e:
    print("❌==========================================❌")
    print("        致命错误：程序核心库载入失败！")
    print("❌==========================================❌")
    traceback.print_exc()
    print("\n请把上面这段英文红色报错排版截图发来！")
    input("按回车键退出程序...")
    sys.exit(1)

# 确保 data 目录存在，避免 sqlite 创建失败
data_dir = BASE_DIR / "data"
os.makedirs(data_dir, exist_ok=True)
origins = [
    "*"  # 测试用，放开所有，生产不要随便用 *
]

app = FastAPI(title="Annual Lucky Draw API")

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix='/api')

# 注册 tortoise 数据库
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 开启自动建表以保证完全跨机器可移植和可自动重新构建
    add_exception_handlers=True,
)

def open_browser():
    time.sleep(1.5)  # 稍微等一秒，确保服务器完全启动
    url = "http://127.0.0.1:8000"
    print(f"🌍 正在打开浏览器访问: {url}")
    webbrowser.open(url)

@app.on_event("startup")
async def load_excel_on_startup():
    """启动时自动导入普通名单和可选的特别大奖名单，保持两个奖池互不覆盖。"""
    
    # 检测到是打包版exe运行时，触发自动弹窗网页
    if getattr(sys, 'frozen', False):
        threading.Thread(target=open_browser, daemon=True).start()
    
    # 兼容打包后 exe 所在的同级目录 / 无论是普通运行还是 exe 运行
    current_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd()
    excel_path = os.path.join(current_dir, "person.xlsx")
    special_excel_candidates = [
        os.path.join(current_dir, "special_person.xlsx"),
        os.path.join(current_dir, "person_special.xlsx"),
    ]
    
    if os.path.exists(excel_path):
        print(f"检测到 {excel_path}，正在自动导入人员名单...")
        try:
            with open(excel_path, "rb") as excel_file:
                contents = excel_file.read()

            participant_list = build_participants_from_excel(contents)
            
            # 普通名单与特别大奖名单分开导入，避免互相覆盖。
            await Participant.all().delete()

            if participant_list:
                await Participant.bulk_create(participant_list)
            print(f"🚀 普通奖池名单自动导入成功，共导入 {len(participant_list)} 条记录！")
        except Exception as e:
            print(f"❌ 导入人员名单失败: {e}")
    else:
        print(f"未在 {current_dir} 检测到 person.xlsx，跳过自动导入。")

    special_excel_path = next(
        (candidate for candidate in special_excel_candidates if os.path.exists(candidate)),
        None,
    )
    if special_excel_path:
        print(f"检测到 {special_excel_path}，正在自动导入特别大奖名单...")
        try:
            with open(special_excel_path, "rb") as excel_file:
                contents = excel_file.read()

            special_participant_list = build_special_participants_from_excel(contents)
            await ParticipantSpecial.all().delete()

            if special_participant_list:
                await ParticipantSpecial.bulk_create(special_participant_list)

            print(f"🚀 特别大奖奖池自动导入成功，共导入 {len(special_participant_list)} 条记录！")
        except Exception as e:
            print(f"❌ 导入特别大奖名单失败: {e}")
    else:
        print(f"未在 {current_dir} 检测到 special_person.xlsx 或 person_special.xlsx，跳过特别大奖名单导入。")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # 允许的源
    allow_credentials=True,       # 允许携带 cookie
    allow_methods=["*"],          # 允许所有方法
    allow_headers=["*"],          # 允许所有请求头
    expose_headers=["Content-Disposition"] 
)

# ================================
# 单机部署：托管静态前端页面
# ================================
if getattr(sys, 'frozen', False):
    # exe 打包后，如果用了 --add-data "static;static"，它会在 _MEIPASS 临时缓存内部
    static_dir = os.path.join(sys._MEIPASS, "static")
else:
    # 源码运行时在 backend/static 目录
    static_dir = os.path.join(BASE_DIR, "static")

if os.path.exists(static_dir):
    # 挂载一些固定的静态资源目录，以提升性能
    _next_dir = os.path.join(static_dir, "_next")
    if os.path.exists(_next_dir):
        app.mount("/_next", StaticFiles(directory=_next_dir), name="next_assets")
        
    images_dir = os.path.join(static_dir, "images")
    if os.path.exists(images_dir):
        app.mount("/images", StaticFiles(directory=images_dir), name="next_images")

    # 捕获所有其他非 api 请求，托管静态文件和前端伪路由
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        if full_path.startswith("api/"):
            return HTMLResponse("API route not found", status_code=404)
            
        static_file_path = os.path.join(static_dir, full_path)
        
        # 1. 寻找确切的文件 (e.g., favicon.ico)
        if full_path and os.path.isfile(static_file_path):
            return FileResponse(static_file_path)
            
        # 2. 寻找 Next.js 生成的 html 路由 (例如 访问 /config 返回 config.html)
        html_file_path = f"{static_file_path}.html"
        if os.path.isfile(html_file_path):
            return FileResponse(html_file_path)
            
        # 3. 兜底返回主页
        index_file = os.path.join(static_dir, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
            
        return HTMLResponse("前端静态文件缺失或尚未编译", status_code=404)
else:
    print("⚠️ 警告：未找到 static 文件夹，前端页面将无法访问。请将 frontend 打包后的 out 文件夹复制为 backend/static。")

# ================================
# 打包入口（给 PyInstaller 用的）
# ================================
if __name__ == "__main__":
    # 添加一个 try-except 捕获所有异常，防止 Windows 双击直接闪退
    try:
        import uvicorn
        import multiprocessing
        # 支持在 Windows 环境下被打包成 exe 后多进程运行稳定
        multiprocessing.freeze_support()
        
        print("🚀 正在启动单机版后台服务...")
        # 打包模式下无需使用字符串加载并关掉热更，可直接跑 app 实例
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("❌ 服务启动失败！如上所示。按回车键退出...")
