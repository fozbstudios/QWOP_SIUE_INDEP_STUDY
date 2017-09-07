class QWOPEnviro(object):
    import socketserver
    import http.server
    import multiprocessing

    # Variables
    PORT = 8081
    URL = 'localhost:{port}'.format(port=PORT)

    # Setup simple sever
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print ("Serving at port", PORT)

    # start the server as a separate process
    server_process = multiprocessing.Process(target=httpd.serve_forever())
    server_process.daemon = True
    server_process.start()
