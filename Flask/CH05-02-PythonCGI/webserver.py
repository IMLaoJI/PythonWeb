import os
# 操作系统相关
from http.server import HTTPServer, CGIHTTPRequestHandler
# CGI:通用网关接口

webdir = '.'  # '.'代表当前目录
port = 80     # 端口

os.chdir(webdir)
server_address = ('', port)
server_obj = HTTPServer(server_address, CGIHTTPRequestHandler)
server_obj.serve_forever()   # 启动服务器


