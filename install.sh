git submodule update --init --recursive
if python3 -c "import virtualenv" &> /dev/null; then #check for virualenv install
    echo ''
else
 	pip3 install virtualenv  
fi

virtualenv QWOPaiVirtualEnv
#activate vintualenv
source QWOPaiVirtualEnv/bin/activate
virtualenv --clear venv
pip3 install --no-cache-dir flask
pip3 install --no-cache-dir flask-socketio
pip3 install --no-cache-dir -U socketIO-client
pip3 install --no-cache-dir tensorflow



