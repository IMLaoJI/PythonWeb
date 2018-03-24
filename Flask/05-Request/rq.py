from flask import Flask, render_template
from flask import request
from urllib.parse import unquote

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])  
def index():
	return render_template('index.html')

@app.route('/reg/')
def reg():
    return render_template('reg.html')

@app.route('/headers/')
def headers():
    data = dict(request.headers)
    return str(data)


@app.route('/rq/')
def get_request():
	path = request.path
	method = request.method
	name = unquote(request.values['name'])
	return name

@app.route('/doreg/', methods=['GET','POST'])
def do_reg():
    name = request.values['username']
    pwd = request.values['pwd']
    # age = request.args.get('age', 0)
    return '姓名:{},密码:{}'.format(name, pwd)

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
