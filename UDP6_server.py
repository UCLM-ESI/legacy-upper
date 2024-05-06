#!/usr/bin/env python3

import socket
import sys


def main(host):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.bind((host, 2000))

    while 1:
        msg, client = sock.recvfrom(1024)
        print(msg.decode(), client)


host = sys.argv[1]

try:
    main(host)
except KeyboardInterrupt:
    print("Server stopped")
    sys.exit(0)


'''
./server.py "::1" &
$ echo hello | ncat -u -6 ::1 2000
New message ('::1', 60440, 0, 0) hello
--
./server.py "" &
$ echo hello | ncat -u -6 ::1 2000
New message ('::1', 60440, 0, 0) hello
$ echo hello | ncat -u -4 127.0.0.1 2000
New message ('::ffff:127.0.0.1', 57305, 0, 0) hello
'''
