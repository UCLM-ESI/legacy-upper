# Python TCP and UDP servers and clients
![test](https://github.com/UCLM-ESI/upper/workflows/test/badge.svg)

These examples implement a very simple service called ``upper``. The ``upper`` servers
reply to the client the uppercase version of the text message that it sends.

As they have a teaching objective. I sacrificed error handling (like exceptions) for
readability and size. A right implementation should add those mechanisms.

You should install ``git`` software and download this repository by this way:

    $ git clone https://github.com/UCLM-ESI/upper.git


## UDP


* [client][udp-client]
* [single process server][udp-server]
* [single process server with SocketServer][udp-SS]    | [doc][socketserver]

* [multiprocess server][udp-fork]                      | [doc][fork]
* [multiprocess server with SocketServer][udp-SS-fork] | [doc][socketserver]

* [async server][udp-asyncio]                          | [doc][asyncio-protocol]


[udp-client]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_client.py
[udp-server]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_server.py
[udp-SS]:     https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_SS.py

[udp-fork]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_fork.py
[udp-SS-fork]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_SS_fork.py
[udp-asyncio]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/UDP_asyncio.py


## TCP

* [client][tcp-client]
* [iterative server][tcp-server]
* [iterative server with SocketServer][tcp-ss]              | [doc][socketserver]

* [forking server][tcp-fork]                                     | [doc][fork]
* [forking server with SocketServer][tcp-ss-fork]                | [doc][socketserver]
* [forking server with multiprocessing.Process][tcp-mp-process]  | [doc][multiprocessing]
* [preforking server with multiprocessing.Pool][tcp-mp-pool]     | [doc][multiprocessing]

* [threaded server][tcp-thread]                                  | [doc][threading]
* [threaded server with SocketServer][tcp-ss-thread]             | [doc][socketserver]

* [async server with select][tcp-select]                                     | [doc][select]
* [async server with selectors][tcp-selectors]                               | [doc][selectors]
* [async server with asyncio transports and protocols][tcp-asyncio-protocol] | [doc][asyncio-protocol]
* [async server with asyncio streams][tcp-asyncio-streams]                   | [doc][asyncio-stream]
* [DEPRECATED] [async server with asyncore][tcp-asyncore]                    | [doc][asyncore]
* [async server with twisted][tcp-twisted]


[tcp-client]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_client.py
[tcp-server]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_server.py
[tcp-ss]:     https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_ss.py

[tcp-fork]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_fork.py
[tcp-ss-fork]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_fork.py
[tcp-mp-process]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_mp_process.py
[tcp-mp-pool]:  https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_mp_pool.py

[tcp-thread]:    https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_thread.py
[tcp-ss-thread]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/tcp_ss_thread.py

[tcp-select]:           https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_select.py
[tcp-selectors]:        https://raw.githubusercontent.com/UCLM-ESI/upper/refs/heads/master/TCP_selectors.py
[tcp-asyncio-protocol]: https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncio_protocol.py
[tcp-asyncio-streams]:  https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncio_streams.py
[tcp-asyncore]:         https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_asyncore.py
[tcp-twisted]:          https://raw.githubusercontent.com/UCLM-ESI/upper/master/TCP_twisted.py

[fork]:             https://docs.python.org/3/library/os.html#os.fork
[threading]:        https://docs.python.org/3/library/threading.html
[socketserver]:     https://docs.python.org/3/library/socketserver.html
[select]:           https://docs.python.org/3/library/socketserver.html
[selectors]:        https://docs.python.org/3/library/selectors.html
[multiprocessing]:  https://docs.python.org/3/library/multiprocessing.html
[asyncio-protocol]: https://docs.python.org/3/library/asyncio-protocol.html
[asyncio-stream]:   https://docs.python.org/3/library/asyncio-stream.html
[asyncore]:         https://docs.python.org/3/library/asyncore.html


## SSL

* [client][ssl-client]
* [SSL server][ssl-server]

[ssl-client]: https://raw.githubusercontent.com/UCLM-ESI/upper/refs/heads/master/SSL_client.py
[ssl-server]: https://raw.githubusercontent.com/UCLM-ESI/upper/refs/heads/master/SSL_server.py


### SSL certs

Generate CA (Certification Authority):

    $ openssl req -x509 -newkey rsa:4096 -keyout ca-key.pem -out ca-cert.pem -nodes -subj "/CN=MyCA"

* ca-key.pem: CA private key
* ca-cert.pem: CA certificate

Generate server private key:

    $ openssl req -newkey rsa:4096 -keyout server-key.pem -out server-req.pem -nodes -subj "/CN=localhost"

* server-key.pem: private server key
* server-req.pem: sign request for CA

Sign server cert with CA:

    $ openssl x509 -req -in server-req.pem -CA ca-cert.pem -CAkey ca-key.pem -CAcreateserial -out server-cert.pem

* server-cert.pem: signed server certificate
