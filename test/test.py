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


class TCPTests(TestCase):
    def setUp(self):
        context.port = 2000

    def run_server(self, prog):
        server = Task(detach=True)
        server.assert_that(localhost,
                           is_not(listen_port(context.port, proto='tcp')))
        server.command("{0} $port".format(prog), timeout=15, expected=None)

        last_client = self.run_clients()
        Task().wait_that(last_client, terminated(), timeout=15)

    def run_clients(self):
        for i in range(10):
            req = 'hello-%s' % i
            client = Task(detach=True)
            client.wait_that(localhost, listen_port(context.port, proto='tcp'))
            client.command('echo %s | ./TCP_client.py localhost $port' % req,
                           timeout=15)
            client.assert_that(client.lastcmd.stdout.content,
                               contains_string("Reply is '" + req.upper()))

        return client

    def test_basic(self):
        self.run_server('./TCP_server.py')

    def test_fork(self):
        self.run_server('./TCP_fork.py')

    def test_process(self):
        self.run_server('./TCP_process.py')

    def test_workers(self):
        self.run_server('./TCP_workers.py')
