#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
from socketserver import DatagramRequestHandler, UDPServer


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


class Handler(DatagramRequestHandler):
    def __init__(self, *args):
        self.n = 0
        DatagramRequestHandler.__init__(self, *args)

    def handle(self):
        self.n += 1
        print("New request: {} {}".format(self.n, self.client_address))
        msg = self.rfile.read()
        self.wfile.write(upper(msg))


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

server = UDPServer(('', int(sys.argv[1])), Handler)
server.serve_forever()
