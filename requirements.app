do shell script "curl -o python-3.6.pkg https://www.python.org/ftp/python/3.6.15/python-3.6.15-macosx10.9.pkg" -- Download Python 3.6
do shell script "sudo installer -pkg python-3.6.pkg -target /" -- Install Python 3.6
do shell script "sudo easy_install pip" -- Install pip
