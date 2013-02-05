.. -*- coding:utf-8 mode:rst -*-

Servidores y clientes UDP y TCP con Python
==========================================

Estos ejemplos implementan un servicio muy simple llamado ``upper``. Los servidores
``upper`` devuelven al cliente la cadena que se le envía (como el servicio ``echo``) pero
transformada a mayúsculas.

Dado que su objetivo es docente, se han sacrificado el control de errores (tal como las
excepciones) en favor de la legibilidad y el tamaño. Una implementación correcta debería
añadir dichos mecanismos.


UDP
---

- Cliente_

.. _Cliente: https://bitbucket.org/arco_group/python-net/raw/49e006731ec9/upper/UDP_client.py
