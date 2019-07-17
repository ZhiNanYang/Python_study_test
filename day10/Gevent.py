#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 08:16:25
# @Author  : Your Name (you@example.org)

import gevent

def func1():
    print(12)
    gevent.sleep(3)
    print(34)

def func2():
    print(56)
    gevent.sleep(1)
    print(78)

def func3():
    print(90)
    gevent.sleep(2)
    print(13)

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func3),
    gevent.spawn(func2)
    ])
