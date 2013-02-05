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

- [Cliente] [udp-client]
- [Servidor síncrono] [udp-server]
- [Servidor multiproceso][udp-fork]
- [Servidor síncrono con SocketServer] [udp-SS]
- [Servidor multiproceso con SocketServer] [udp-SS-fork]


[udp-client]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_client.py
[udp-server]:    https://bitbucket.org/arco_group/upper/raw/tip/UDP_server.py
[udp-fork]:      https://bitbucket.org/arco_group/upper/raw/tip/UDP_fork_server.py
[udp-SS]:        https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS_server.py
[udp-SS-fork]:   https://bitbucket.org/arco_group/upper/raw/tip/UDP_SS_fork_server.py


TCP
---
