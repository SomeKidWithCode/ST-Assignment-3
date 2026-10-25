REM Quick util file that executes all tests on Windows 10/11
REM Does not work on any OS other than windows

@echo off

echo "Running python tests..."

python -m pytest -vv

echo "Python testing finished"

pause
