import os
from dotenv import load_dotenv
from pathlib import Path
"""
# 第一次初始化
aerich init -t app.db.TORTOISE_ORM

# 初始建表
aerich init-db

# 修改模型后
aerich migrate 生成迁移文件
aerich upgrade 应用迁移文件
"""

# 取到 backend/ 目录的绝对路径，确保执行路径正确
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# 默认连接本地 MySQL 数据库
DB_URL = os.environ.get("DB_URL")

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}
