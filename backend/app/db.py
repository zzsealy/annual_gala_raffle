import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# 取到执行路径，确保 exe 和源码运行时路径均正确
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# 默认连接本地数据库
DB_URL = os.environ.get("DB_URL")

# 处理 SQLite 在 exe 下的动态绝对路径问题，确保把 data 库创建在 exe 的同级目录下
if DB_URL and DB_URL.startswith("sqlite://") and "://" in DB_URL:
    db_relative_path = DB_URL.split("sqlite://")[1]
    if not os.path.isabs(db_relative_path):
        absolute_db_path = BASE_DIR / db_relative_path
        absolute_db_path.parent.mkdir(parents=True, exist_ok=True)
        DB_URL = f"sqlite://{absolute_db_path}"

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
