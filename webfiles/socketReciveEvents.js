socket.on('pressQ', function() {
    //simulate Q press
    console.log("got pressQ event!!!")
});
socket.on('pressW', function() {
    //simulate W press
    console.log("got pressW event!!!")
});
socket.on('pressO', function() {
    //simulate O press
    console.log("got pressO event!!!")
});
socket.on('pressP', function() {
    //simulate P press
    console.log("got pressP event!!!")
});


function testMouseDown(){
    var mde= new Event('mousedown');
    t=document.getElementById('gameContent');
    t.dispatchEvent(mde);
}
function testKeyDown(){
    var event = document.createEvent('Event'); event.initEvent('keydown', true, false /*event type, buble through dom?, cancelable?*/); event.keyCode = 76;
}
testMouseDown();