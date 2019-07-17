#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-24 08:19:11
# @Author  : Your Name (you@example.org)

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost"))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print('[x] %r' % body)


channel.basic_consume(queue_name, callback)
channel.start_consuming()
