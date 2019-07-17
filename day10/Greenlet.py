#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 17:25:53
# @Author  : Your Name (you@example.org)

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
