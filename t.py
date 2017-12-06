import threading
from server import QWOPInputOutput as a 

def work():
    while True:
        b=3

def cTh():
    s=a()
    s.connectAI()
    s.socketio.emit("test")

th = threading.Thread(target=work)
tr = threading.Thread(target=cTh)
th.start()
tr.start()

