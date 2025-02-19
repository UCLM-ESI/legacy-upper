#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
import socket
import multiprocessing as mp

MAX_CHILDREN = 10


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def handle(sock, client):
    print(f"Client connected: {client}")
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
        pass


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', int(sys.argv[1])))
    sock.listen(5)

    workers = []
    for i in range(10):
        ps = mp.Process(target=server, args=[sock])
        ps.start()
        workers.append(ps)

    for w in workers:
        w.join()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__.format(sys.argv[0]))
        sys.exit(1)

    try:
        main()
    except KeyboardInterrupt:
        print("shut down")
