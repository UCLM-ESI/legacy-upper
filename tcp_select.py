#!/usr/bin/python3
# Copyright: See AUTHORS and COPYING
"Usage: {0} <port>"

import sys
import select
import time
import socket
from utils import show_select_status


def upper(msg):
    time.sleep(1)  # simulates a complex job
    return msg.upper()


def master_handler(socks, master):
    conn, client = master.accept()
    socks.append(conn)
    print(f"- Client connected: {client}, Total {len(socks)} sockets")


def child_handler(socks, conn):
    data = conn.recv(32)
    if not data:
        socks.remove(conn)
        conn.close()
        return

    conn.sendall(upper(data))


def main(port):
    master = socket.socket()
    master.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master.bind(('', port))
    master.listen(5)
    socks = [master]

    while 1:
        read_ready = select.select(socks, [], [])[0]
        show_select_status(socks, set(read_ready))
        for s in read_ready:
            if s == master:
                master_handler(socks, s)
            else:
                child_handler(socks, s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.format(sys.argv[0]))
        sys.exit(1)

    main(int(sys.argv[1]))
