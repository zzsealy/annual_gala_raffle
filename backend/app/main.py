import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.db import TORTOISE_ORM, BASE_DIR
from app.api import router as api_router

# 确保 data 目录存在，避免 sqlite 创建失败
data_dir = BASE_DIR / "data"
os.makedirs(data_dir, exist_ok=True)

app = FastAPI(title="Annual Lucky Draw API")

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix='/api')

# 注册 tortoise 数据库
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # 因为使用 aerich 进行数据库迁移，所以这里设为 False
    add_exception_handlers=True,
)
