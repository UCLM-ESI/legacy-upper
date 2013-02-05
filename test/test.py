#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

from hamcrest import is_not, contains_string
from prego import TestCase, Task, context, terminated
from prego.net import localhost, listen_port


class UDPTests(TestCase):
    def test_udp_sync(self):
        context.port = 2000

        server = Task(detach=True)
        server.assert_that(localhost,
                           is_not(listen_port(context.port, proto='udp')))
        server.command('./UDP_server.py $port', timeout=15, expected=None)

        for i in range(10):
            req = 'hello-%s' % i
            client = Task(detach=True)
            client.wait_that(localhost, listen_port(context.port, proto='udp'))
            client.command('echo %s | ./UDP_client.py localhost $port' % req,
                           timeout=15)
            client.assert_that(client.lastcmd.stdout.content,
                               contains_string("Reply is '" + req.upper()))

        Task().wait_that(client, terminated(), timeout=15)
