#!/usr/bin/python3 -u
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import struct
import socket

MCAST_GROUP = '239.0.0.1'


def handle(sock, msg, client, n):
    print(f"New message {n} {client}")
    print(msg.decode())


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((MCAST_GROUP, int(sys.argv[1])))

    group = struct.pack('4sL', socket.inet_aton(MCAST_GROUP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, group)

    n = 0
    while 1:
        msg, client = sock.recvfrom(1024)
        n += 1
        handle(sock, msg, client, n)


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    print("exited")
