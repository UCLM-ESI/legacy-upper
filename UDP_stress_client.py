#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port> <n_clients> <message>"

import sys
import threading
import _thread as thread
import time
import select
import socket

TIMEOUT = 8

host = sys.argv[1]
port = int(sys.argv[2])
nclients = int(sys.argv[3])
message = sys.argv[4]


def client(n):
    global r
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '{0} [{1}]'.format(message, n).encode()
    sock.sendto(data, (host, port))
    rd = select.select([sock], [], [], TIMEOUT)[0]
    if rd == []:
        print('- ERROR: Client {0:3} was not answered after {1}s'.format(n, TIMEOUT))
        r += 1
        return

    msg, server = sock.recvfrom(1024)
    print("Received: {0}".format(msg))
    sock.close()


if len(sys.argv) != 5:
    print(__doc__.format(__file__))
    sys.exit(1)

workers = []


for n in range(nclients):
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

print('- Clients never served: {}'.format(r))
