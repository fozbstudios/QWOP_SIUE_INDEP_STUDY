if python3 -c "import virtualenv" &> /dev/null; then #check for virualenv install
    echo ''
else
 	pip install virtualenv  
fi

virtualenv ..
#activate

pip install -e gym
pip install -e gym-http-api