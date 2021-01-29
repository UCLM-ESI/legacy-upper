Python-3 TCP and UDP servers and clients
========================================

These examples implement a very simple service called ``upper``. The ``upper`` servers
reply to the client the uppercase version of the text message that it sends.

As they have a teaching objective. I sacrificed error handling (like exceptions) for
readability and size. A right implementation should add that mechanisms.

You should install ``git`` software in your computer and download this repository with next command:

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
* [synchronous server with SocketServer][tcp-SS]

* [forking server][tcp-fork]
* [forking server with SocketServer][tcp-SS-fork]
* [forking server with Process][tcp-process]
* [preforking server (process workers)][tcp-worker]

* [threaded server][tcp-thread]
* [threaded server with SocketServer][tcp-SS-thread]

* [async server with select][tcp-select]
* [async server with asyncore][tcp-asyncore]
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

[tcp-select]:   https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_select.py
[tcp-asyncore]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncore.py
[tcp-twisted]:  https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_twisted.py
