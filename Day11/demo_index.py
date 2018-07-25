#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Sebastian Williams

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("12121212")
        u = self.get_argument("user")
        e = self.get_argument("email")
        p = self.get_argument("pwd")
        print(u, e, p)
        if u == "chenshuo" and e == "chenshuo@qq.com" and p == "chenshuo":
            self.write("登录成功")
        else:
            self.write("密码或用户名错误")


application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

"""运行该脚本，依次执行：

    创建一个Application对象，并把一个正则表达式'/'和类名MainHandler传入构造函数：tornado.web.Application(...)　　
    执行Application对象的listen(...)方法，即：application.listen(8888)
    执行IOLoop类的类的 start() 方法，即：tornado.ioloop.IOLoop.instance().start()

整个过程其实就是在创建一个socket服务端并监听8888端口，当请求到来时，根据请求中的url和请求方式（post、get或put等）来指定相应的类中的方法来处理本次请求，在上述demo中只为url为http://127.0.0.1:8888/index的请求指定了处理类MainHandler（具体如何寻找见下文）。所以，在浏览器上访问：http://127.0.0.1:8888/index，则服务器给浏览器就会返回 Hello,world ，否则返回 404: Not Found（tornado内部定义的值）， 即完成一次http请求和响应。
由上述分析，我们将整个Web框架分为两大部分：

    待请求阶段，即：创建服务端socket并监听端口
    处理请求阶段，即：当有客户端连接时，接受请求，并根据请求的不同做出相应的相应
"""
