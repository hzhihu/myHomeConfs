#!/usr/bin/env python
# coding:utf-8

import web

from services.MsgSender import MsgSender
from services.DreamCubeTop import DreamCubeTop
from services.DreamTreeTop import DreamTreeTop
from services.Robots import Robots

urls = (
		'/send', "MsgSender",
		'/send/', "MsgSender",

		'/cubetop', "DreamCubeTop",
		'/cubetop/', "DreamCubeTop",
		'/cubetop/count(\d+)/index(\d+)', "DreamCubeTop",
		'/cubetop/count(\d+)/index(\d+)/', "DreamCubeTop",
		'/cubetop/count(\d+)', "DreamCubeTop",
		'/cubetop/count(\d+)/', "DreamCubeTop",

		'/treetop', "DreamTreeTop",
		'/treetop/', "DreamTreeTop",
		'/treetop/count(\d+)', "DreamTreeTop",
		'/treetop/count(\d+)/', "DreamTreeTop",
		'/treetop/count(\d+)/index(\d+)', "DreamTreeTop",
		'/treetop/count(\d+)/index(\d+)/', "DreamTreeTop",

		'/robots', "Robots",
		'/robots/', "Robots",
		'/robots/count(\d+)', "Robots",
		'/robots/count(\d+)/', "Robots",
		'/robots/count(\d+)/index(\d+)', "Robots",
		'/robots/count(\d+)/index(\d+)/', "Robots",

		'/', "index"
	)

class index:
    """索引"""
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        i = 0
        output = []
        output.append("<h2>Index</h2>")
        output.append("<ul>")
        classes=[]
        while True:
            if len(urls) - i < 2:
                break
            key=urls[i]
            i+=1
            value=urls[i]
            i+=1
            if value not in classes:
                classes.append(value)
                output.append("<li><a href='%s'>%s  --  %s</a> %s" % (key, key, value, eval(value).__doc__))
                if key == '/send':
                    output.append("<p>USAGE: wget -qSO- %s://%s/send --post-data 'POST DATA as message content.'</p>" % (web.ctx.protocol, web.ctx.host))
                output.append("</li>")
        output.append("</ul>")
        return "\n".join(output)
    def POST(self):
        return web.seeother("/")

app = web.application(urls, locals())

if __name__ == '__main__':
    # 如果要用于 fcgi 取消下面的注释
	# web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()