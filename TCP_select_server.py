#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys, select, time
from socket import *

def upper(msg):
    time.sleep(1)
    return msg.upper()

def ChildHandler(s):
    data = s.recv(32)
    if not data:
        socks.remove(s)
        s.close()
        return

    s.sendall(upper(data))

def ParentHandler(s):
    child_sock, client = s.accept()
    socks.append(child_sock)
    print('Client connected: {0}, Total {1} sockets'.format(
        client, len(socks)))


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

ss = socket(AF_INET, SOCK_STREAM)
ss.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ss.bind(('', int(sys.argv[1])))
ss.listen(5)

socks = [ss]

while 1:
    rd = select.select(socks, [], [])[0]

    print socks
    print rd

    for i in rd:
        if i == ss:
            ParentHandler(i)
        else:
            ChildHandler(i)
