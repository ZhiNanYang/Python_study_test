#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 12:42:14
# @Author  : Your Name (you@example.org)

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue_name,
                      callback)
channel.start_consuming()
