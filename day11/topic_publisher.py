#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 13:02:00
# @Author  : Your Name (you@example.org)

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
msg = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=msg)
print(" [x] Sent %r:%r" % (routing_key, msg))
connection.close()
