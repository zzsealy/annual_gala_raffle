import multiprocessing

if __name__ == "__main__":
    # Windows多进程环境稳定支持
    multiprocessing.freeze_support()
    
    print("🚀 正在启动单机版后台服务...")
    # 集中捕获整体应用的启动异常
    try:
        from app.main import app
        import uvicorn
        
        # 启动 ASGI 服务
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        import traceback
        import sys
        
        err_text = traceback.format_exc()
        print("❌==========================================❌")
        print("        致命错误：程序核心库载入失败！")
        print("❌==========================================❌")
        print(err_text)
        print("\n[为了方便排查，报错已经写入 error_report.txt]")
        
        with open("error_report.txt", "w", encoding="utf-8") as f:
            f.write("FATAL IMPORT CRASH:\n")
            f.write(err_text)

        input("按回车键退出程序...")
        sys.exit(1)
