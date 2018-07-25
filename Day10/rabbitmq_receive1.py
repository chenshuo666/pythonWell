#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

'''You may ask why we declare the queue again ‒ we have already declared it in our previous code.
We could avoid that if we were sure that the queue already exists. For example if send.py program
was run before. But we're not yet sure which program to run first. In such cases it's a good
practice to repeat declaring the queue in both programs.'''

channel.queue_declare(queue='hello3',durable=True)#如果接收端先运行的话，没有队列会进行报错


def callback(ch, method, properties, body):#回调函数
    print(ch,'----',method,'----',properties,'----',body)

    print(" [x] Received %r" % body)


channel.basic_qos(prefetch_count=1)#限制队列中有一条消息没处理完，就不会发送

#消费消息，仅仅是声明语法
channel.basic_consume(callback,#如果收到消息，就调用callback来处理消息
                      queue='hello3',#声明要收消息的队列
                      # no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()