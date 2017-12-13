 var socket = io.connect('http://' + document.domain + ':' + location.port);
function sendCurScore(cs){
    socket.emit('current score', cs);
    wait=new XMLHttpRequest
    wait.open('GET',"mutex.txt",false); //block until file returned
    wait.send(null);
}
function sendFinScore(fs){
    socket.emit('final score', fs);
    wait=new XMLHttpRequest
    wait.open('GET',"mutex.txt",false); //block until file returned
    wait.send(null);
}
function sendStart(){
    socket.emit('start');
    wait=new XMLHttpRequest
    console.log("Should not be dead anymore")
    wait.open('GET',"mutex.txt",false); //block until file returned
    wait.send(null);
}
function sendDeath(){
    socket.emit('death');
    wait=new XMLHttpRequest
    wait.open('GET',"mutex.txt",false); //block until file returned
    wait.send(null);
}
function sendLife(){
    socket.emit('life')
    wait=new XMLHttpRequest
    wait.open('GET',"mutex.txt",false); //block until file returned
    wait.send(null);
};
