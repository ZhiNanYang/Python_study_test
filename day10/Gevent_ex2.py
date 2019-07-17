#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 12:40:34
# @Author  : Your Name (you@example.org)

from gevent import monkey
monkey.patch_all()
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
