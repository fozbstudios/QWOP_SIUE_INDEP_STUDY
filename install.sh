$cond1 = "$BASH_SOURCE[0]" = "$0" &> /dev/null;
$cond2 = '${(%):-%x}' = "$0" &> /dev/null;
if  $cond1 || $cond2; then
    echo "you are runnning me correctly. I am being sourced"
    if python -c "import virtualenv" &> /dev/null; then #check for virualenv install
        echo ''
    else
        pip install virtualenv  
    fi

     virtualenv QWOPaiVirtualEnv
    #activate vintualenv
    source ./QWOPaiVirtualEnv/bin/activate
    pip install --no-cache-dir flask
    pip install --no-cache-dir flask-socketio
    pip install socketIO-client-2
    pip install --no-cache-dir tensorflow
    source "" &> /dev/null #clear source
else
    echo "error: im not breing run from source. Do: source $0 " 2> /dev/null
    echo "$SHELL"
    echo "$0"
    source "" &> /dev/null #clear source
    echo "exiting"
fi
