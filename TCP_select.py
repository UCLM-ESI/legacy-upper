#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import select
import time
import socket


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def child_handler(sock):
    data = sock.recv(32)
    if not data:
        socks.remove(sock)
        sock.close()
        return

    sock.sendall(upper(data))


def master_handler(sock):
    child_sock, client = sock.accept()
    socks.append(child_sock)
    print("+ Client connected: {}, Total {} sockets".format(
        client, len(socks)))


def show_status(socks, read):
    def socket_peer(sock):
        try:
            return sock.getpeername()
        except OSError:
            return "master"

    print("open:  {}\nready: {}\n---".format(
        [socket_peer(x) for x in socks],
        [socket_peer(x) for x in read_ready]))


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind(('', int(sys.argv[1])))
ss.listen(30)

socks = [ss]

while 1:
    read_ready = select.select(socks, [], [])[0]

    for i in read_ready:
        if i == ss:
            master_handler(i)
        else:
            child_handler(i)

    show_status(socks, read_ready)
