#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import SocketServer, time

def upper(msg):
    time.sleep(1)
    return msg.upper()

class UpperHandler(SocketServer.DatagramRequestHandler):
    def __init__(self, *args):
        self.n = 0
        SocketServer.DatagramRequestHandler.__init__(self, *args)

    def handle(self):
        self.n += 1
        print('New request:', self.n, self.client_address)
        msg = self.rfile.read()
        self.wfile.write(upper(msg))


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

server = SocketServer.UDPServer(('', int(sys.argv[1])), UpperHandler)
server.serve_forever()
