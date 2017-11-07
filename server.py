#!/Usr/bin/python
import time
from flask import Flask,request, redirect, url_for, send_from_directory

from socketIO_client import SocketIO as SocClient
from flask_socketio import SocketIO
class QWOPInputOutput:
    def __init__(self):
        #self.app = Flask(__name__,static_folder='webfiles');
        self.socketio = SocClient('localhost',5000)
        self.died=False
        self.curScore=0
        self.tickCount=0
        self.finScore=0
        self.QPressed=False
        self.WPressed=False
        self.OPressed=False
        self.PPressed=False
        self.firstRun=True



        @self.socketio.on('connect')
        def hc():
            print('connect\n\n\n')
        #@self.socketio.on('current score')
        #def hc(cs):
            #print(repr(cs) +'\n\n\n')
        @self.socketio.on('final score')
        def hc(self, fs):
            #print(repr(cs) +'\n\n\n')
            self.finScore=fs
            self.QPressed=False
            self.WPressed=False
            self.OPressed=False
            self.PPressed=False
            self.curScore=0
            self.tickCount=0
            self.died=True
        @self.socketio.on('current score')
        def hc(self, cs):
            self.curScore=cs
            self.tickCount+=1

        @self.socketio.on('serverReady')
        def hc(self):
            # print('clicking\n\n\n')
            self.died=False;
            if self.firstRun==True:
                self.socketio.emit('aiReady')
                self.firstRun=False
    def controlManage(self, eventStr):
        if eventStr=="pQ":
            self.QPressed=True;self.socketio.emit('pressQ')
        elif eventStr=="pW":
            self.WPressed=True;self.socketio.emit('pressW')
        elif eventStr=="pO":
            self.OPressed=True;self.socketio.emit('pressO')
        elif eventStr=="pP":
            self.PPressed=True;self.socketio.emit('pressP')
        elif eventStr=="rQ":
            self.QPressed=False;self.socketio.emit('releaseQ')
        elif eventStr=="rW":
            self.WPressed=False;self.socketio.emit('releaseW')
        elif eventStr=="rO":
            self.OPressed=False;self.socketio.emit('releaseO')
        elif eventStr=="rP":
            self.PPressed=False;self.socketio.emit('releaseP')
        else:# bad arg
            errStr="eventStr %s is undefined!" % eventStr
            raise NameError(errStr)
if __name__ == '__main__':
        app = Flask(__name__,static_folder='webfiles');

        # Routes
        @app.route('/')
        def root():
            return app.send_static_file('index.html')

        @app.route('/<path:path>')
        def static_proxy(path):
            # send_static_file will guess the correct MIME type
          return app.send_static_file(path)
        socketiorunner = SocketIO(app)
        socketiorunner.run(app)
