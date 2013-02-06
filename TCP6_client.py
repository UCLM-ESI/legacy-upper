#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port>"

import sys
import socket


def main():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((sys.argv[1], int(sys.argv[2]), 0, 0))

    while 1:
        data = sys.stdin.readline().strip()
        if not data:
            break

        sent = sock.send(data)

        msg = ''
        while len(msg) < sent:
            msg += sock.recv(32)

        print("Reply is '{0}'".format(msg))

    sock.close()

if len(sys.argv) != 3:
    print(__doc__.format(__file__))
    sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    pass
