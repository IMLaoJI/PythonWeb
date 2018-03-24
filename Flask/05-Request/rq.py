from flask import Flask, render_template
from flask import request
from urllib.parse import unquote

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/rq/')
def get_request():
	path = request.path
	method = request.method
	name = unquote(request.args.get('name','未找到'))
	return name

if __name__ == '__main__':
	app.run()
	
#--------------------------------

# CMD控制台使用以下代码模拟上下文
# context = app.test_request_context('/rq/')
# context.push()

# 测试
# request.path
# request.method

# 退出
## request.pop()

#--------------------------------

# 特殊字符编码
# import urllib.parse
# urllib.parse.quote('tom&jerry#? mike')
