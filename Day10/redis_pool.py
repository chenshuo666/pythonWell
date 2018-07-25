#!/usr/bin/python
#-*- coding:utf-8 -*-
# Author:Sebastian Williams

import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379)

r= redis.Redis(connection_pool=pool)
pipe=r.pipeline(transaction=True)

pipe.set('name','chenshuo')

pipe.set('sex','boy')
pipe.execute( )
