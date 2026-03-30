@echo off
echo Starting Windows Build...
echo.

if not exist venv\Scripts\activate.bat goto skip_venv
echo Activating virtual environment...
call venv\Scripts\activate.bat
goto finish_venv

:skip_venv
echo WARNING: backend\venv not found! Using global python environment.

:finish_venv
echo.
echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Cleaning previous builds...
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist

echo.
echo Running PyInstaller...
pyinstaller --name "AnnualRaffle" --noconfirm --onedir --add-data "static;static" --hidden-import="app.models" --hidden-import="aerich.models" --hidden-import="aiosqlite" --hidden-import="tortoise.backends.sqlite" --hidden-import="pydantic.v1" --hidden-import="uvicorn.logging" --hidden-import="uvicorn.loops" --hidden-import="uvicorn.loops.auto" --hidden-import="uvicorn.protocols" --hidden-import="uvicorn.protocols.http" --hidden-import="uvicorn.protocols.http.auto" --hidden-import="uvicorn.protocols.websockets" --hidden-import="uvicorn.protocols.websockets.auto" --hidden-import="uvicorn.lifespan" --hidden-import="uvicorn.lifespan.on" app/main.py

echo.
if errorlevel 1 (
    echo [ERROR] PyInstaller failed! Please check the output above.
) else (
    echo SUCCESS! Build complete.
    echo Your application is inside the "dist" directory.
)
pause
