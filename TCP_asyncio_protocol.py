#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
import asyncio


def upper(msg):
    time.sleep(1)
    return msg.upper()


class UpperProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.peername = transport.get_extra_info("peername")
        print("Client connected: {}".format(self.peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()

        reply = upper(message)
        self.transport.write(reply.encode())

    def connection_lost(self, exc):
        print("Client disconnected: {}".format(self.peername))
        self.transport.close()


async def main(port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(UpperProtocol, '', port)

    async with server:
        await server.serve_forever()


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

asyncio.run(main(sys.argv[1]))
