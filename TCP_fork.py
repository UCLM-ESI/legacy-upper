#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import os
import time
import socket


class ProcessPool(object):
    def __init__(self, max_children=40):
        self.max_children = max_children
        self.children = []

    # from SocketServer (at Python std lib)
    def collect_children(self):
        while self.children:
            if len(self.children) < self.max_children:
                opts = os.WNOHANG
            else:
                opts = 0

            pid, status = os.waitpid(0, opts)
            if not pid:
                break

            self.children.remove(pid)

    def start_new_process(self, func, args):
        self.collect_children()
        pid = os.fork()
        if pid:
            self.children.append(pid)
        else:
            func(*args)
            sys.exit()


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def handle(sock, client, n):
    print(f"Client {n:>3} connected: {client}")
    while 1:
        data = sock.recv(32)
        if not data:
            break
        sock.sendall(upper(data))

    sock.close()
    print(f"Client {n:>3} disconnected: {client}")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', int(sys.argv[1])))
    sock.listen(30)

    pool = ProcessPool()
    n = 0

    while 1:
        conn, client = sock.accept()
        pool.start_new_process(handle, (conn, client, n := n+1))


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    print("shut down")
