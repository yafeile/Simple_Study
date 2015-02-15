#! /usr/bin/env/python
# -*- coding:utf-8 -*-

import os
import SocketServer

class ForkingEchoRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = '%s:%s' % (cur_pid,data)
        self.request.send(response)
        return

class ForkingEchoServer(SocketServer.ForkingMixIn,
                                      SocketServer.TCPServer
                                      ):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost',0)
    server = ForkingEchoServer(address,ForkingEchoRequestHandler)
    ip,port = server.server_address # what port was assigned?
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()
    print 'Server loop running in process:',os.getpid()

    # Connect to the server
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))

    # Send the data
    message = 'Hello,world'
    print 'Sending:"%s"'%message
    len_sent = s.send(message)

    # Receive a response
    response = s.recv(1024)
    print 'Received:"%s"'%response

    # Clean up
    server.shutdown()
    s.close()
    server.socket.close()