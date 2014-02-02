#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port> <n_clients> <message>"

import sys
import threading
import thread
import time
import select
import socket

TIMEOUT = 8


def client(n):
    global r
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto('{0} [{1}]'.format(sys.argv[4], n),
                (sys.argv[1], port))
    rd = select.select([sock], [], [], TIMEOUT)[0]
    if rd == []:
        print('{0} does not reply'.format(n))
        r += 1
        return

    msg, server = sock.recvfrom(1024)
    print("Received: '{0}'".format(msg))
    sock.close()


if len(sys.argv) != 5:
    print(__doc__.format(__file__))
    sys.exit(1)

workers = []

port = int(sys.argv[2])

for n in range(int(sys.argv[3])):
    worker = threading.Thread(target = client, args = (n,))
    workers.append(worker)

r = 0
n = 0
while n < len(workers):
    try:
        workers[n].start()
    except thread.error as e:
        print(e)
        time.sleep(0.5)
        continue
    n += 1

for w in workers:
    w.join()

print("{0} did not reply".format(r))
