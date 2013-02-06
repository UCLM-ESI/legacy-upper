Servidores y clientes UDP y TCP con Python
==========================================

Estos ejemplos implementan un servicio muy simple llamado ``upper``. Los servidores
``upper`` devuelven al cliente la cadena que se le envía (como el servicio ``echo``) pero
transformada a mayúsculas.

Dado que su objetivo es docente, se han sacrificado el control de errores (tal como las
excepciones) en favor de la legibilidad y el tamaño. Una implementación correcta debería
añadir dichos mecanismos.

Puedes descargar este repositorio completo con:

    :::bash
    $ hg clone https://bitbucket.org/arco_group/upper


UDP
---

- [Cliente] [udp-client]
- [Servidor síncrono] [udp-server]
- [Servidor multiproceso][udp-fork]
- [Servidor síncrono con SocketServer] [udp-SS]
- [Servidor multiproceso con SocketServer] [udp-SS-fork]


[udp-client]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_client.py
[udp-server]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_server.py
[udp-fork]:      https://bitbucket.org/arco_group/upper/raw/tip/UDP_fork.py
[udp-SS]:        https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS.py
[udp-SS-fork]:   https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS_fork.py


TCP
---

- [Cliente] [tcp-client]
- [Servidor síncrono] [tcp-server]
- [Servidor síncrono con SocketServer] [tcp-SS]

- [Servidor multiproceso][tcp-fork]
- [Servidor multiproceso con SocketServer] [tcp-SS-fork]
- [Servidor multiproceso con Process] [tcp-process]
- [Servidor con process workers (preforking)] [tcp-worker]

- [Servidor multihilo][tcp-thread]
- [Servidor multihilo con SocketServer] [tcp-SS-thread]

- [Servidor asíncrono con select] [tcp-select]
- [Servidor asíncrono con asyncore] [tcp-asyncore]
- [Servidor asíncrono con twisted] [tcp-twisted]


[tcp-client]:    https://bitbucket.org/arco_group/upper/raw/tip/TCP_client.py
[tcp-server]:    https://bitbucket.org/arco_group/upper/raw/tip/TCP.py
[tcp-SS]:        https://bitbucket.org/arco_group/upper/raw/tip/TCP_SS.py

[tcp-fork]:      https://bitbucket.org/arco_group/upper/raw/tip/TCP_fork.py
[tcp-SS-fork]:   https://bitbucket.org/arco_group/upper/raw/tip/TCP_SS_fork.py
[tcp-process]:   https://bitbucket.org/arco_group/upper/raw/tip/TCP_process.py
[tcp-worker]:    https://bitbucket.org/arco_group/upper/raw/tip/TCP_worker.py

[tcp-thread]:    https://bitbucket.org/arco_group/upper/raw/tip/TCP_thread.py
[tcp-SS-thread]: https://bitbucket.org/arco_group/upper/raw/tip/TCP_SS_thread.py

[tcp-select]:    https://bitbucket.org/arco_group/upper/raw/tip/TCP_select.py
[tcp-asyncore]:  https://bitbucket.org/arco_group/upper/raw/tip/TCP_asyncore.py
[tcp-twisted]:   https://bitbucket.org/arco_group/upper/raw/tip/TCP_twisted.py

<!--
-- Local Variables:
--  coding: utf-8
--  mode: flyspell
--  ispell-local-dictionary: "castellano"
-- End:
-->
