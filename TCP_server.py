#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys, time
from socket import *

def upper(msg):
    time.sleep(1)
    return msg.upper()

def handle(sock, client):
    print('Client connected: {0}'.format(client))
    while 1:
        data = sock.recv(32)
        if not data: break
        sock.sendall(upper(data))

    sock.close()
    print('Client disconnected: {0}'.format(client))


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', int(sys.argv[1])))
sock.listen(1)

while 1:
    child_sock, client = sock.accept()
    handle(child_sock, client)
