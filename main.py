from nickQWOPai import QWOPai
from server import QWOPInputOutput

import webbrowser, os
import threading
import time
import eventlet
from flask import Flask,request, redirect, url_for, send_from_directory, render_template, send_file
from array import array

import socketio as SocServer
from socketIO_client import SocketIO as SocClient

if __name__ == '__main__':
# eventlet.monkey_patch()                                                                           
    app = Flask(__name__,static_folder='webfiles')                                                         
    clients=[]                                                                                          
    # Routes                                                                                           
    @app.route('/')                                                                                     
    def root():                                                                                        
        # return app.send_static_file('index.html')                                                     
        # return render_template('index.html')                                                          
        return send_file('webfiles/index.html')                                                         
    def threadWork():                                                                                   
        eventlet.wsgi.server(eventlet.listen(('', 5001)), app);                                         
    @app.route('/<path:path>')                                                                          
    def static_proxy(path):                                                                             
        # send_static_file will guess the correct MIME type                                             
        # return render_template(path)                                                                  
        return send_file('webfiles/'+path)
    webbrowser.open("localhost:5001")
    socketiorunner = SocServer.Server()                                                                 
    # socketiorunner = SocServer.Server(app, debug=True,async_mode='eventlet')                          
    app=SocServer.Middleware(socketiorunner,app)                                                        
    # app.wsgi_app=SocServer.Middleware(socketiorunner,app)                                             
     # eventlet.wsgi.server(eventlet.listen(('', 5001)), app);                                           
    ai = QWOPai()
    print("Running ai")
    ai.run()

    thr= threading.Thread(target=threadWork)                                                            
    thr.start()                                                                                         
    # socketiorunner.run(app)                                                                           
    @socketiorunner.on("serverReady")                                                                   
    def test(sid):                                                                                      
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
    @socketiorunner.on("connection")                                                                    
    def cc(sid, environ):                                                                               
        print("server recieved connection")                                                             
        clients.append(sid)                                                                             
                                                                                                        
    @socketiorunner.on("test")                                                                          
    def cw(sid):                                                                                        
        print("server recieved connection")                                                             
        print("emmitting")                                                                              
        socketiorunner.emit("aiReady")                                                                  
    @socketiorunner.on("current score")                                                                 
    def csSend(sid,css):                                                                                
        #print(css)                                                                                     
        #print('a')                                                                                     
        socketiorunner.emit("current score",data=css)
