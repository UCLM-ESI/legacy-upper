#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import os
import time
import socket
from multiprocessing import Process

MAX_PROCS = 10


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def handle(sock, client):
    print(f"Client connected: {client}, PID: {os.getpid()}")
    while 1:
        data = sock.recv(32)
        if not data:
            break
        sock.sendall(upper(data))

    sock.close()
    print(f"Client disconnected: {client}")


def server(sock):
    try:
        while 1:
            conn, client = sock.accept()
            handle(conn, client)
    except KeyboardInterrupt:
        sys.exit(0)


def main(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(5)

    procs = [Process(target=server, args=[sock]) for _ in range(MAX_PROCS)]
    for p in procs:
        p.start()

    for p in procs:
        p.join()


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

try:
    main(int(sys.argv[1]))
except KeyboardInterrupt:
    print("shut down")
