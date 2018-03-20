from flask import Flask, render_template
from flask import request, make_response
from flask import Response


app = Flask(__name__)

@app.route('/')
def home():
    return "网站首页"

@app.route('/hello/<name>/')
def hello(name):
    return "您好:" + name

@app.route('/greeting/')
def greeting():
    name = "Eason"
    employees = [
    {"id": 1, "name": "Tom", "email": "tom@tom.com"}.
    {"id": 1, "name": "Jerry", "email": "tom@tom.com"}.
    {"id": 1, "name": "Mike", "email": "tom@tom.com"}.
    {"id": 1, "name": "Peter", "email": "tom@tom.com"}.
    ]
    return render_template('hello.html', name=name, employees=employees)

@app.route('/req/')
def request_obj():
    return render_template('req.html', req=request)

@app.route('/reg/')
def reg():
    return render_template('reg.html')

@app.route('/getdata/')
def get_data():
    username = request.args.get('username', None)
    email = request.args.get('email', None)
    return username + ', ' = email

@app.route('/postdata/', method=['POST'])
def post_data():
    if request.method == 'POST'
        username = request.form.get('username', None)
        email = request.form.get('email', None)
        return f"有数据提交过来,用户名:{username},邮箱:{email}"
    return "没有数据提交"

@app.route('/rsp/')
def custom_response():
    rsp = make_response(render_template('xxx.html', foo=20), 200)
    rsp.headers['X-Value'] = "8139fd183ghhdf10adasd"  # 增加头部信息,用于反爬取
    return rsp
