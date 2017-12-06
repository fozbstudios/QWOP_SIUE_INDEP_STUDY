 var socket = io.connect('http://' + document.domain + ':' + location.port);
function sendCurScore(cs){
    socket.emit('current score', cs);
}
function sendFinScore(fs){
    socket.emit('final score', fs);
}
function sendStart(){
    socket.emit('start');
    console.log("Should not be dead anymore")
}
function sendDeath(){
    socket.emit('death');
}
function sendLife(){
    socket.emit('life')
};
