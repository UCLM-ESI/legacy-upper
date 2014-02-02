#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port> <n_clients>"

import sys
import threading
import thread
import time
import select
import socket

TIMEOUT = 30
queries = ['hello', 'world', 'bye', 'people']


def client(n):
    global r
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((sys.argv[1], port))

    for q in queries:
        data = '{0} [{1}]'.format(q, n)
        sock.send(data)

        reply = ''
        while len(reply) < len(data):
            rd = select.select([sock], [], [], TIMEOUT)[0]
            if not rd:
                print('- Client {0} does not respond after {1}s'.format(n, TIMEOUT))
                r += 1
                return

            reply += sock.recv(32)

        print("- Received: '{0}'".format(reply))

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

if r:
    print('- {0} clients did not reply'.format(r))
