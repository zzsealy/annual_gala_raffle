import os
import sys
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
from app.models import Participant

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

# 注册 tortoise 数据库 (它会在内部注册 startup 事件)
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # 因为使用 aerich 进行数据库迁移，所以这里设为 False
    add_exception_handlers=True,
)

def open_browser():
    time.sleep(1.5)  # 稍微等一秒，确保服务器完全启动
    url = "http://127.0.0.1:8000"
    print(f"🌍 正在打开浏览器访问: {url}")
    webbrowser.open(url)

@app.on_event("startup")
async def load_excel_on_startup():
    """每次启动时，如果是单机执行文件，就弹网页；如果根目录下存在 person.xlsx，就自动读取覆盖数据库内容"""
    
    # 检测到是打包版exe运行时，触发自动弹窗网页
    if getattr(sys, 'frozen', False):
        threading.Thread(target=open_browser, daemon=True).start()
    
    # 兼容打包后 exe 所在的同级目录 / 无论是普通运行还是 exe 运行
    current_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.getcwd()
    excel_path = os.path.join(current_dir, "person.xlsx")
    
    if os.path.exists(excel_path):
        print(f"检测到 {excel_path}，正在自动导入人员名单...")
        try:
            df = pd.read_excel(excel_path, engine='openpyxl')
            participant_list = []
            
            # 删除旧数据，防止每次启动重复插入
            await Participant.all().delete()

            for val_a, val_f in zip(df.iloc[:, 0], df.iloc[:, 5]):
                participant_list.append(Participant(
                    code=str(val_a),
                    name=str(val_f)
                ))
            await Participant.bulk_create(participant_list)
            print(f"🚀 人员名单自动导入成功，共导入 {len(participant_list)} 条记录！")
        except Exception as e:
            print(f"❌ 导入人员名单失败: {e}")
    else:
        print(f"未在 {current_dir} 检测到 person.xlsx，跳过自动导入。")

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
    import uvicorn
    import multiprocessing
    # 支持在 Windows 环境下被打包成 exe 后多进程运行稳定
    multiprocessing.freeze_support()
    
    print("🚀 正在启动单机版后台服务...")
    # 打包模式下无需使用字符串加载并关掉热更，可直接跑 app 实例
    uvicorn.run(app, host="0.0.0.0", port=8000)
