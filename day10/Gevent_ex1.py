#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 12:31:00
# @Author  : Your Name (you@example.org)

import gevent


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
