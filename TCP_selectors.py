#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import socket
import selectors
import time


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def child_handler(sock):
    data = sock.recv(32)
    if not data:
        selector.unregister(sock)
        sock.close()
        return

    sock.sendall(upper(data))


def master_handler(sock):
    conn, client = sock.accept()
    selector.register(conn, selectors.EVENT_READ, child_handler)
    print("+ Client connected: {}".format(client))


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

ss = socket.socket()
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('', int(sys.argv[1])))
ss.listen(30)

selector = selectors.DefaultSelector()
selector.register(ss, selectors.EVENT_READ, master_handler)

while True:
    for key, mask in selector.select():
        key.data(key.fileobj)
