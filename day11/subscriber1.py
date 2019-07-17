#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-27 17:53:38
# @Author  : Your Name (you@example.org)

from redishelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
