#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()#声明一个管道

# 声明queue
channel.queue_declare(queue='hello3',durable=True)#队列持久化，不丢失，只能把队列持久化，重启时，消息还是会消失

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello3',#queue的名字
                      body='Hello World2!',#声明要发送的内容
                      properties=pika.BasicProperties(delivery_mode=2,)#消息持久化
                      )

print(" [x] Sent 'Hello World!'")
connection.close()