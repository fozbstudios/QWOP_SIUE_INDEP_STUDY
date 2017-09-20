#!/usr/bin/python
from flask import Flask,request, redirect, url_for, send_from_directory

import time
from flask_socketio import SocketIO

app = Flask(__name__,static_folder='webfiles');
socketio = SocketIO(app)
app.debug = True


# Routes
@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

@socketio.on('connect')
def hc():
    print('connect\n\n\n')
    
@socketio.on('serverReady')
def hc():
    print('clicking\n\n\n')
    socketio.emit('aiReady')
if __name__ == '__main__':
    socketio.run(app)
    
