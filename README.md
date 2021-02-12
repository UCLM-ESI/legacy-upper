Python-3 TCP and UDP servers and clients
========================================

These examples implement a very simple service called ``upper``. The ``upper`` servers
reply to the client the uppercase version of the text message that it sends.

As they have a teaching objective. I sacrificed error handling (like exceptions) for
readability and size. A right implementation should add those mechanisms.

You should install ``git`` software and download this repository by this way:

    $ git clone https://github.com/UCLM-ESI/upper.git


UDP
---

* [client][udp-client]
* [synchronous server][udp-server]
* [synchronous server with SocketServer][udp-SS]

* [multiprocess server][udp-fork]
* [multiprocess server with SocketServer][udp-SS-fork]


[udp-client]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_client.py
[udp-server]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_server.py
[udp-SS]:     https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_SS.py

[udp-fork]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_fork.py
[udp-SS-fork]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_SS_fork.py


TCP
---

* [client][tcp-client]
* [synchronous server][tcp-server]
* [synchronous server with SocketServer][tcp-SS] ([doc](https://docs.python.org/3/library/socketserver.html))

* [forking server][tcp-fork]
* [forking server with SocketServer][tcp-SS-fork]
* [forking server with multiprocessing.Process][tcp-process]
* [preforking server with multiprocessing.Process)][tcp-prefork]

* [threaded server][tcp-thread]
* [threaded server with SocketServer][tcp-SS-thread]

* [async server with select][tcp-select] ([doc](https://docs.python.org/3/library/select.html))
* [async server with asyncio transports and protocols][tcp-asyncio-protocol] ([doc](https://docs.python.org/3/library/asyncio-protocol.html))
* [async server with asyncio streams][tcp-asyncio-streams] ([doc](https://docs.python.org/3/library/asyncio-stream.html))
* [DEPRECATED] [async server with asyncore][tcp-asyncore] ([doc](https://docs.python.org/3/library/asyncore.html))
* [async server with twisted][tcp-twisted]


[tcp-client]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_client.py
[tcp-server]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_server.py
[tcp-SS]:     https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_SS.py

[tcp-fork]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_fork.py
[tcp-SS-fork]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_SS_fork.py
[tcp-process]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_process.py
[tcp-worker]:  https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_workers.py

[tcp-thread]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_thread.py
[tcp-SS-thread]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_SS_thread.py

[tcp-select]:           https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_select.py
[tcp-asyncio-protocol]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncio_protocol.py
[tcp-asyncio-streams]:  https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncio_streams.py 
[tcp-asyncore]:         https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncore.py
[tcp-twisted]:          https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_twisted.py
