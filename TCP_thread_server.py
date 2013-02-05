#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys, thread, time
import socket

def upper(msg):
    time.sleep(1)
    return msg.upper()

def handle(sock, client, n):
    print 'Client connected', n, client
    while 1:
        data = sock.recv(32)
        if not data: break
        sock.sendall(upper(data))
    sock.close()


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', int(sys.argv[1])))
sock.listen(5)

n = 0
while 1:
    child_sock, client = sock.accept()
    n += 1
    thread.start_new_thread(handle, (child_sock, client, n))
