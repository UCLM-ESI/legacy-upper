.. -*- coding:utf-8 mode:rst -*-

Servidores y clientes UDP y TCP con Python
==========================================

Estos ejemplos implementan un servicio muy simple llamado ``upper``. Los servidores
``upper`` devuelven al cliente la cadena que se le envía (como el servicio ``echo``) pero
transformada a mayúsculas.

Dado que su objetivo es docente, se han sacrificado el control de errores (tal como las
excepciones) en favor de la legibilidad y el tamaño. Una implementación correcta debería
añadir dichos mecanismos.

Puedes descargar este repositorio completo con::

  $ hg clone https://bitbucket.org/arco_group/upper


UDP
---

- [Cliente][udp-client]
- [Servidor síncrono[udp-server]

<!--
- `Servidor multiproceso`_
- `Servidor síncrono con SocketServer`_
- `Servidor multiproceso con SocketServer`_
-->

[udp-client]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_client.py
[udp-server]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_server.py

.. _Servidor Multiproceso:
   https://bitbucket.org/arco_group/upper/raw/tip/UDP_fork_server.py

.. _Servidor síncrono con SocketServer:
   https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS_server.py

.. _Servidor multiproceso con SocketServer:
   https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS_fork_server.py


TCP
---

- `Cliente`_
- `Servidor Síncrono`_
- `Servidor multiproceso`_
- `Servidor multihilo`_
- `Servidor síncrono con SocketServer`_
- `Servidor multiproceso con SocketServer`_
- `Servidor multihilo con SocketServer`_


.. _Cliente:
   https://bitbucket.org/arco_group/upper/raw/tip/TCP_client.py

.. _Servidor Síncrono:
   https://bitbucket.org/arco_group/upper/raw/tip/TCP_server.py

.. _Servidor Multiproceso:
   https://bitbucket.org/arco_group/upper/raw/tip/TCP_fork_server.py

.. _Servidor síncrono con SocketServer:
   https://bitbucket.org/arco_group/upper/raw/tip/TCP_SS_server.py

.. _Servidor multiproceso con SocketServer:
   https://bitbucket.org/arco_group/upper/raw/tip/TCP_SS_fork_server.py
