#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys, time
import SocketServer

def upper(msg):
    time.sleep(1)
    return msg.upper()

class UpperHandler(SocketServer.DatagramRequestHandler):
    def handle(self):
        print('New request: {0}'.format(self.client_address))
        msg = self.rfile.read()
        self.wfile.write(upper(msg))


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

srv = SocketServer.ForkingUDPServer(('', int(sys.argv[1])), UpperHandler)
srv.serve_forever()
