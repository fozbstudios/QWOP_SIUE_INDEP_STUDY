#!/usr/bin/python
import time
from flask import Flask,request, redirect, url_for, send_from_directory
from array import array

from socketIO_client import SocketIO as SocClient
from flask_socketio import SocketIO
class QWOPInputOutput:
    def __init__(self):
        #self.app = Flask(__name__,static_folder='webfiles');
        self.socketio = SocClient('localhost',5000)
        self.died=True
        self.curScore=0
        self.tickCount=0
        self.finScore=0
        self.QPressed=False
        self.WPressed=False
        self.OPressed=False
        self.PPressed=False
        self.firstRun=True
        self.keyDurations=array('Q',[0,0,0,0]) # unsigned long long 


        self.socketio.on('connect', self.con)
        self.socketio.on('final score',self.fsf)
        self.socketio.on('current score', self.csf)
        self.socketio.on('serverReady',self.srf)
    def srf(self):
        # print('clicking\n\n\n')
        self.died=False
        if self.firstRun==True:
            self.socketio.emit('aiReady')
    def con(self):
        print('connect\n\n\n')
        #self.socketio.on('current score')
        #def hc(cs):
        #print(repr(cs) +'\n\n\n')
        self.firstRun=False
    def fsf(self, fs):
        #print(repr(cs) +'\n\n\n')
        self.finScore=fs
        self.QPressed=False
        self.WPressed=False
        self.OPressed=False
        self.PPressed=False
        self.curScore=0
        self.tickCount=0
        self.died=True

    def csf(self, cs):
        self.curScore=cs
        self.tickCount+=1
        for i in range(len(self.keyDurations)):
            if self.keyDurations[i] >0:
                self.keyDurations[i] -= 1
            if self.keyDurations[i]<0:
                self.keyDurations[i] += 1
            # if self.keyDurations[i]<=0:
            #     if i==0:
            #         self.controlManage("rQ")
            #     elif i==1:
            #         self.controlManage("rW")
            #     elif i==2:
            #         self.controlManage("rO")
            #     elif i==3:
            #         self.controlManage("rP")


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
    # def actionChooser(self,actionNum,tickDuration):
    def actionChooser(self,actionNum):
        self.controlManage("rQ")
        self.controlManage("rW")
        self.controlManage("rO")
        self.controlManage("rP")
        if actionNum==0: #do nothing
            for item in self.keyDurations:
                # item-=tickDuration
        elif actionNum == 1: #Q
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
        elif actionNum == 2: #W
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
        elif actionNum == 3: #O
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
        elif actionNum == 4: #P
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 5: #QW
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
        elif actionNum == 6: #QO
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
        elif actionNum == 7: #QP
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 8: #WO
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
        elif actionNum == 9: #WP
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 10: #OP
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 11: #QWO
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
        elif actionNum == 12: #QWP
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 13: #QOP
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 14: #WOP
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
        elif actionNum == 15: #QWOP
            self.controlManage("pQ")
            # self.keyDurations[0]+=tickDuration
            self.controlManage("pW")
            # self.keyDurations[1]+=tickDuration
            self.controlManage("pO")
            # self.keyDurations[2]+=tickDuration
            self.controlManage("pP")
            # self.keyDurations[3]+=tickDuration
if __name__ == '__main__':
    app = Flask(__name__,static_folder='webfiles')

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
    @socketiorunner.on("serverReady")
    def test():
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressQ")
        socketiorunner.emit("pressW")
        socketiorunner.emit("pressW")
        socketiorunner.emit("pressW")
        socketiorunner.emit("pressW")
        socketiorunner.emit("pressO")
        socketiorunner.emit("pressO")
        socketiorunner.emit("pressO")
        socketiorunner.emit("pressO")
        socketiorunner.emit("pressP")
        socketiorunner.emit("pressP")
        socketiorunner.emit("pressP")
