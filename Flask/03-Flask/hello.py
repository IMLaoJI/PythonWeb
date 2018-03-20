from flask import Flask


app = Flask(__name__)  # 告知flask站点起始位置就是本文件(hello.py)所在位置
app.debug = True       # 设置调试属性, 自动侦测代码改动并重启服务器

@app.route('/hello')   # 路由绑定函数: 在地址栏写入/hello时执行以下函数, /hello/不可执行
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        <h1>Hello 优品课堂</h1>
    </body>
    </html>"""
    return html

@app.route('/')        # 匹配多个地址
@app.route('/uke/')    # 路由绑定函数: 在地址栏写入/uke/或/uke时执行以下函数
def greeting():
    return "您好: 优品课堂"

if __name__ == '__main__':
    app.run()
