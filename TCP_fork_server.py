#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys, os, time
import socket

class ProcessPool:
    def __init__(self, max_children=40):
        self.max_children = max_children
        self.children = []

    # taken from SocketServer (at Python std lib)
    def collect_children(self):
        while self.children:
            if len(self.children) < self.max_children:
                opts = os.WNOHANG
            else:
                opts = 0

            pid, status = os.waitpid(0, opts)
            if not pid: break
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

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', int(sys.argv[1])))
    sock.listen(5)

    pool = ProcessPool()
    n = 0

    while 1:
        child_sock, client = sock.accept()
        n += 1
        pool.start_new_process(handle, (child_sock, client))


if len(sys.argv) != 2:
    print(__doc__.format(__file__))
    sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    sys.exit(0)
