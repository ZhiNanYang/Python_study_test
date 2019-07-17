#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 07:44:22
# @Author  : Your Name (you@example.org)

import pika
import sys


connetion = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connetion.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

msg = ' '.join(sys.argv[1:]) or 'info: Hello World!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=msg)
print("[x] Sent %r" % msg)
connetion.close()
