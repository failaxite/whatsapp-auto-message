@echo off
set pythonVersion=3.6.15
set pythonInstallerURL=https://www.python.org/ftp/python/%pythonVersion%/python-%pythonVersion%-amd64.exe

:: Download Python installer
curl -o python-installer.exe %pythonInstallerURL%

:: Install Python
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_pip=1

:: Remove the installer
del python-installer.exe

:: Upgrade pip
python -m ensurepip --default-pip
python -m pip install --upgrade pip
