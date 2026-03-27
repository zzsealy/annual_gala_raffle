import os
import sys
import pandas as pd
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
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

@app.on_event("startup")
async def load_excel_on_startup():
    """每次启动时，如果根目录下存在 person.xlsx，就自动读取覆盖数据库内容"""
    
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
