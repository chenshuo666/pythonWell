#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout'#fanout: 所有bind到此exchange的queue都可以接收消息
                         )

result=channel.queue_declare(exclusive=True)#不指定queue的名字，rabbit会自动分配一个名字

queue_name = result.method.queue
print(queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name
                   )

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
