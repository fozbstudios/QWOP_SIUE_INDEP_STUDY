#!python
#!/usr/bin/python
import eventlet
eventlet.monkey_patch()
import threading 
import time
from flask import Flask,request, redirect, url_for, send_from_directory, render_template, send_file
from array import array

import socketio as SocServer
from socketIO_client import SocketIO as SocClient

from nickQWOPai import QWOPai as q
def spawnThread():
    ai=q()
    t=threading.Thread(target=q.runAI)
app = Flask(__name__,static_folder='webfiles')
# Routes
@app.route('/')
def root():
    # return app.send_static_file('index.html')
    # return render_template('index.html')
    return send_file('webfiles/index.html')
socketiorunner = SocServer.Server(app, debug=True,async_mode='eventlet')
@socketiorunner.on("connection")
def cc(sid, environ):
    print("server recieved connection")

@socketiorunner.on("test")
def cw(sid):
    print("server recieved connection")
    print("emmitting")
    socketiorunner.emit("aiReady")
@socketiorunner.on("current score")
def csSend(sid,css):
    print(css)
    print('a')
    socketiorunner.emit("current score",data=css)
@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    # return render_template(path)
    return send_file('webfiles/'+path)
app=SocServer.Middleware(socketiorunner,app)
# app.wsgi_app=SocServer.Middleware(socketiorunner,app)
spawnThread()
eventlet.wsgi.server(eventlet.listen(('', 5001)), app);

