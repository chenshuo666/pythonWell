#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout'
                         #fanout: 所有bind到此exchange的queue都可以接收消息
                         )



# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.


message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                      )
print(" [x] Sent %r" % message)
connection.close()