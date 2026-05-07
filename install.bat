@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo SysML v2 Automated Validation Pipeline Setup
echo ========================================================
echo.

:: 1. Check for Git
where git >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Git is not installed or not found in PATH.
    echo Please install Git from https://git-scm.com/
    exit /b 1
)
echo [OK] Git is installed.

:: 2. Check for Python
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python is not installed or not found in PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    exit /b 1
)
echo [OK] Python is installed.

:: 3. Setup SysML v2 Validator directory
set V2_DIR=..\sysml-validator
if exist "%V2_DIR%" (
    echo [OK] SysML v2 Validator repository already exists at %V2_DIR%.
) else (
    echo [INFO] Cloning turbogeek SysML v2 Validator repository...
    git clone https://github.com/turbogeek/sysmlv2-validator.git "%V2_DIR%"
    if !ERRORLEVEL! neq 0 (
        echo [ERROR] Failed to clone the repository. Please check your internet connection or Git configuration.
        exit /b 1
    )
    echo [OK] Cloned sysmlv2-validator to %V2_DIR%.
)

:: 4. Configure Java via CATIA Magic / Cameo
echo.
echo ========================================================
echo Java Configuration (CATIA Magic / Cameo)
echo ========================================================
echo The validation pipeline requires a Java runtime. It is highly recommended 
echo to use the JRE bundled with your CATIA Magic / Cameo Systems Modeler installation.
echo.

set /p CAMEO_DIR="Enter the full path to your Cameo installation (e.g. C:\Program Files\Cameo Systems Modeler) or press ENTER to skip: "

if "%CAMEO_DIR%"=="" (
    echo [INFO] Skipping Cameo Java configuration. Ensure Java is in your PATH.
    goto :end
)

:: Remove surrounding quotes if present
set CAMEO_DIR=%CAMEO_DIR:"=%

set JRE_BIN=%CAMEO_DIR%\jre\bin\java.exe

if not exist "%JRE_BIN%" (
    echo [ERROR] Could not find java.exe at "%JRE_BIN%".
    echo Please ensure the path is correct and points to the root Cameo directory.
    goto :end
)

echo [OK] Found Cameo bundled Java at "%JRE_BIN%".

set /p SET_JAVA="Do you want to set JAVA_HOME and add it to your PATH? (y/n): "
if /i "!SET_JAVA!"=="y" (
    :: Set JAVA_HOME permanently for the user
    setx JAVA_HOME "%CAMEO_DIR%\jre"
    
    :: Add to User PATH if not already present
    echo [INFO] Adding Java to User PATH...
    for /f "skip=2 tokens=3*" %%a in ('reg query HKCU\Environment /v PATH') do set USER_PATH=%%a %%b
    echo !USER_PATH! | find /i "%CAMEO_DIR%\jre\bin" > nul
    if !ERRORLEVEL! neq 0 (
        setx PATH "%CAMEO_DIR%\jre\bin;!USER_PATH!"
        echo [OK] Added Java to PATH.
    ) else (
        echo [INFO] Java is already in your PATH.
    )
    
    echo [OK] JAVA_HOME has been set. You MUST restart your terminal for these changes to take effect.
)

:end
echo.
echo ========================================================
echo Setup Complete! You are ready to run the validation scripts.
echo ========================================================
pause
