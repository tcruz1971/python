#!/usr/bin/python
"""
Forking TCP server for handling client requests
"""

import os, SocketServer, commands


class ForkingOwnServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """ adds ForkingMixIn """
    pass



class OwnRequestHandler(SocketServer.StreamRequestHandler):
    """ handles requests from clients """
    def handle(self):
        myRoot = '/home/tcruz/pyFunctions/'
        task = self.request.recv(4096)
        myFunc = task.split()[0]
        if os.path.exists(myRoot + myFunc):
            self.request.sendall(commands.getoutput(myRoot + task))
        else:
            self.request.sendall(myFunc + ' is not a valid function, try one of these:\n'
                                  + commands.getoutput('cd ' + myRoot + '; ls newweb*'))
        return

if __name__ == '__main__':
    # from now on we dwell in the land of daemons
    if os.fork():
        os._exit(0)
    os.setsid()

    # insure we are not a session leader
    if os.fork():
        os._exit(0)

    # non comunicado
    os.close(0)
    os.close(1)
    os.close(2)

    # start the server
    server = ForkingOwnServer(('192.168.0.30', 41236), OwnRequestHandler)
    server.serve_forever()
