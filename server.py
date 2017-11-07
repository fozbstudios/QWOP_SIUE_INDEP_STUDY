#!/Usr/bin/python
from flask import Flask,request, redirect, url_for, send_from_directory

import time
from flask_socketio import SocketIO
class QWOPInputOutput:
    def __init__(self):
        self.app = Flask(__name__,static_folder='webfiles');
        self.socketio = SocketIO(app)
        self.died=False
        self.curScore=0
        self.tickCount=0
        self.finScore=0
        self.QPressed=False
        self.WPressed=False
        self.OPressed=False
        self.PPressed=False
        self.firstRun=True


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
        #@socketio.on('current score')
        #def hc(cs):
            #print(repr(cs) +'\n\n\n')
        @socketio.on('final score')
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
        @socketio.on('current score')
        def hc(self, cs):
            self.curScore=cs
            self.tickCount+=1

        @socketio.on('serverReady')
        def hc(self):
            # print('clicking\n\n\n')
            self.died=False;
            if self.firstRun==True:
                socketio.emit('aiReady')
                self.firstRun=False
    def controlManage(self, eventStr):
        if eventStr=="pQ":
            self.QPressed=True;socketio.emit('pressQ')
        elif eventStr=="pW":
            self.WPressed=True;socketio.emit('pressW')
        elif eventStr=="pO":
            self.OPressed=True;socketio.emit('pressO')
        elif eventStr=="pP":
            self.PPressed=True;socketio.emit('pressP')
        elif eventStr=="rQ":
            self.QPressed=False;socketio.emit('releaseQ')
        elif eventStr=="rW":
            self.WPressed=False;socketio.emit('releaseW')
        elif eventStr=="rO":
            self.OPressed=False;socketio.emit('releaseO')
        elif eventStr=="rP":
            self.PPressed=False;socketio.emit('releaseP')
        else:# bad arg
            errStr="eventStr %s is undefined!" % eventStr
            raise NameError(errStr)
if __name__ == '__main__':

    socketio.run(app)
