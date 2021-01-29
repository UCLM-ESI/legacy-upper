#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


class Upper(Protocol):
    def connectionMade(self):
        print("Client connected: {}".format(self.transport.client))

    def connectionLost(self, reason):
        print("Client disconnected: {}".format(self.transport.client))

    def dataReceived(self, data):
        self.transport.write(upper(data))


class UpperFactory(Factory):
    protocol = Upper


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

reactor.listenTCP(int(sys.argv[1]), UpperFactory())
reactor.run()
