#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 13:14:04
# @Author  : Your Name (you@example.org)

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for bingding_key in binding_keys:
    channel.queue_bind(queue=queue_name,
                       exchange='topic_logs',
                       routing_key=bingding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue_name, callback)
channel.start_consuming()
