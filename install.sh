git submodule update --init --recursive
if python3 -c "import virtualenv" &> /dev/null; then #check for virualenv install
    echo ''
else
 	pip3 install virtualenv  
fi

virtualenv QWOPaiVirtualEnv
#activate vintualenv
source QWOPaiVirtualEnv/bin/activate
pip3 install flask
pip3 install flask-socketio
pip3 install tensorflow



