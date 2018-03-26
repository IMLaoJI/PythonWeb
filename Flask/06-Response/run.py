from flask import Flask, request, make_response, render_template, redirect, url_for, abort
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    # 创建一个响应对象response
    resp = make_response()                           # 创建响应
    resp.response = render_template('index.html')    # 响应内容
    resp.headers['Content-type'] = 'text/html'       # ContentType
    resp.status_code = 200                           # 指定状态码
    # resp.status = '200'
    return resp

@app.route('/a/')
def rq_a():
    # return redirect(url_for('rq_b'))
    return render_template('page-a.html')

@app.route('/help/?id=5')
def req_help():
    abort(404)

@app.route('/about-us/')
def rq_b():
    return render_template('page-b.html')

@app.route('/rq/')
def test_rq():
    data = {}
    data['ip'] = request.remote_addr
    data['full_path'] = request.full_path
    data['url'] = request.url
    data['is_xhr'] = request.is_xhr
    data['endpoint'] = request.endpoint

    return str(data)

@app.route('/user/')
def user_info():
    name = 'Tom'

    return render_template('user-info.html', name=name)

if __name__ == '__main__':
    app.run()
