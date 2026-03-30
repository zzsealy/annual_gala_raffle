@echo off
rem Start Windows Build

rem 1. Activate venv
if not exist venv\Scripts\activate.bat goto skip_venv
echo Activating local environment...
call venv\Scripts\activate.bat
goto finish_venv
:skip_venv
echo WARNING: Local environment not found. Using global.
:finish_venv

rem 2. Install Pyinstaller
pip install pyinstaller

rem 3. Clean
if exist build rmdir /S /Q build
if exist dist rmdir /S /Q dist

rem 4. Package
echo Packaging Application...
pyinstaller ^
  --name "AnnualRaffleSystem" ^
  --noconfirm ^
  --onedir ^
  --add-data "static;static" ^
  --hidden-import="app.models" ^
  --hidden-import="aerich.models" ^
  --hidden-import="aiosqlite" ^
  --hidden-import="tortoise.backends.sqlite" ^
  --hidden-import="pydantic.v1" ^
  --hidden-import="uvicorn.logging" ^
  --hidden-import="uvicorn.loops" ^
  --hidden-import="uvicorn.loops.auto" ^
  --hidden-import="uvicorn.protocols" ^
  --hidden-import="uvicorn.protocols.http" ^
  --hidden-import="uvicorn.protocols.http.auto" ^
  --hidden-import="uvicorn.protocols.websockets" ^
  --hidden-import="uvicorn.protocols.websockets.auto" ^
  --hidden-import="uvicorn.lifespan" ^
  --hidden-import="uvicorn.lifespan.on" ^
  app/main.py

echo Build completed! 
echo Open dist\AnnualRaffleSystem folder and copy your .env and person.xlsx into it!
pause
