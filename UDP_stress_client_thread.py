#!/usr/bin/env python3
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


class ClientError(Exception):
    pass


class Client(threading.Thread):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.was_ok = True

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            for query in queries:
                data = '{0} [{1}]'.format(query, self.index).encode()
                self.sock.sendto(data, (host, port))
                reply = self.receive()
                print(f"Received: {reply}")
        except ClientError as e:
            print(e)
            self.was_ok = False

        self.sock.close()

    def receive(self):
        rd = select.select([self.sock], [], [], TIMEOUT)[0]
        if rd == []:
            raise ClientError("- ERROR: Client {0:3} didn't get reply after {1}s".format(
                self.index, TIMEOUT))

        reply, server = self.sock.recvfrom(1024)
        return reply


if len(sys.argv) != 4:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
nclients = int(sys.argv[3])

clients = [Client(n) for n in range(nclients)]

for client in clients:
    try:
        client.start()
    except thread.error as e:
        print(e)
        time.sleep(0.5)

for w in clients:
    w.join()

print("- Clients never served: {}".format(
    len([c for c in clients if not c.was_ok])))
