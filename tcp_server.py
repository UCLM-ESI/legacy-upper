#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
import socket


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def handle(sock):
    while 1:
        data = sock.recv(32)
        if not data:
            break

        sock.sendall(upper(data))

    sock.close()


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', int(sys.argv[1])))
sock.listen(5)

while 1:
    conn, client = sock.accept()
    print(f"Client connected: {client}")
    handle(conn)
    print(f"Client disconnected: {client}")
