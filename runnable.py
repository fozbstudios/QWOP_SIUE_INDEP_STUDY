#!python
#!/usr/bin/python
import eventlet
# eventlet.monkey_patch()
import threading 
import time
from flask import Flask,request, redirect, url_for, send_from_directory, render_template, send_file
from array import array

import webbrowser, os
import socketio as SocServer
from socketIO_client import SocketIO as SocClient

from nickQWOPai import QWOPai as q
def spawnThread():
    ai=q()
    t=threading.Thread(target=ai.runAI)
    t.start()
app = Flask(__name__,static_folder='webfiles')
socketiorunner = SocServer.Server( debug=True,async_mode='eventlet')
@app.route('/')
def root():
    # return app.send_static_file('index.html')
    # return render_template('index.html')
    return send_file('webfiles/index.html')
@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    # return render_template(path)
    return send_file('webfiles/'+path)
@socketiorunner.on("serverReady")
def test(sid):
    print("serverready")
    # socketiorunner.emit("pressP")
@socketiorunner.on("connection")
def cc(sid, environ):
    print("server recieved connection")

@socketiorunner.on("final score")
def fsSend(sid,fss):
    print("Final Score")
    print(fss)
    

@socketiorunner.on("start")
def ss(sid, st):
    print("Started")

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

spawnThread()
app=SocServer.Middleware(socketiorunner,app)
eventlet.wsgi.server(eventlet.listen(('', 5001)), app);

