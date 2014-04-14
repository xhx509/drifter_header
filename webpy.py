# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:56:23 2013

@author: hxu
"""

import web
import socket

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        socket.settimeout()
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()