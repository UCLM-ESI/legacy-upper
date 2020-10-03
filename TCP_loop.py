#!/usr/bin/python3 

import time
import asyncio


def upper(msg):
    time.sleep(1)
    return msg.upper()


class UpperProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        
        reply = upper(message)
        self.transport.write(reply.encode())

    def connection_lost(self, exc):
        self.transport.close()


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: UpperProtocol(), '', 2000)

    async with server:
        await server.serve_forever()


asyncio.run(main())