 var socket = io.connect('http://' + document.domain + ':' + location.port);
function sendCurScore(cs){
    socket.emit('current score', cs);
}
function sendFinScore(fs){
    socket.emit('final score', fs);
}
function sendStart(){
    socket.emit('start');
}
