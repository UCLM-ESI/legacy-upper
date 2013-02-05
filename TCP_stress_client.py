#!/usr/bin/python
# Copyright: See AUTHORS and COPYING
"Usage: {0} <host> <port> <n_clients>"

import sys, threading, thread, time, select
from socket import *

TIMEOUT = 30

msglist = ['hello', 'world', 'bye', 'people']

def client(n):
    global r
    end = False
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((sys.argv[1], port))
    for cad in msglist:
        data = '{0} [{1}]'.format(cad, n)
        sock.send(data)

        reply = ''
        while len(reply) < len(data):
            rd = select.select([sock], [], [], TIMEOUT)[0]
            if rd == []:
                print('No response:', n)
                r += 1
                end = True
                break
            reply += sock.recv(32)

        if end: break
        print "Received: '{0}'".format(reply)

    sock.close()


if len(sys.argv) != 4:
    print(__doc__.format(__file__))
    sys.exit(1)


threads = []

port = int(sys.argv[2])

for n in range(int(sys.argv[3])):
    worker = threading.Thread(target = client, args = (n,))
    threads.append(worker)

r = 0
n = 0
while n < len(threads):
    try:
        threads[n].start()
    except thread.error, e:
        print e
        time.sleep(.1)
        continue
    n += 1

for w in threads:
    w.join()

print('did not reply', r)
