#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import time
import asyncio


def upper(msg):
    time.sleep(1)
    return msg.upper()


async def handle(reader, writer):
    peername = writer.get_extra_info('peername')
    print("Client connected: {}".format(peername))

    while 1:
        data = await reader.read(32)
        if not data:
            break
        writer.write(upper(data))
        await writer.drain()

    print(f"Client disconnected: {peername}")
    writer.close()


async def main(port):
    server = await asyncio.start_server(handle, '', port)

    async with server:
        await server.serve_forever()


if len(sys.argv) != 2:
    print(__doc__.format(sys.argv[0]))
    sys.exit(1)

try:
    asyncio.run(main(sys.argv[1]))
except KeyboardInterrupt:
    print("exited")
