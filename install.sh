git submodule update --init --recursive
if python3 -c "import virtualenv" &> /dev/null; then #check for virualenv install
    echo ''
else
 	pip install virtualenv  
fi

virtualenv QWOPaiVirtualEnv
#activate vintualenv
source QWOPaiVirtualEnv/bin/activate
pip install flask-socketio
npm install requirejs
npm install socket.io
npm install express



