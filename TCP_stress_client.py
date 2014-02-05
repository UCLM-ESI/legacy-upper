#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port> <n_clients>"

import sys
import threading
import _thread as thread
import time
import select
import socket

TIMEOUT = 30
queries = "twenty tiny tigers take two taxis to town".split()


def client(n):
    global r
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((sys.argv[1], port))

    for q in queries:
        data = '{0} [{1}]'.format(q, n).encode()
        sock.send(data)

        reply = bytes()
        while len(reply) < len(data):
            rd = select.select([sock], [], [], TIMEOUT)[0]
            if not rd:
                print('- ERROR: Client {0:3} was not answered after {1}s, aborting'.format(
                    n, TIMEOUT))
                r += 1
                return

            try:
                reply += sock.recv(32)
            except ConnectionResetError:
                print('- ERROR: Client {0:3}: connection reset'.format(n))
                return

        print("- Received: {0}".format(reply))

    sock.close()


if len(sys.argv) != 4:
    print(__doc__.format(__file__))
    sys.exit(1)


threads = []
port = int(sys.argv[2])
nclients = int(sys.argv[3])

for n in range(nclients):
    threads.append(threading.Thread(target = client, args = (n,)))

r = 0

for t in threads:
    try:
        t.start()
    except thread.error as e:
        print(e)
        time.sleep(.1)

for t in threads:
    t.join()

print('- Clients never served: {}'.format(r))
