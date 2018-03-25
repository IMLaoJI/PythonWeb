from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '首页'

@app.route('/rq/')
def test_rq():
    data = {}
    data['ip'] = request.remote_addr
    data['full_path'] = request.full_path
    data['url'] = request.url
    data['is_xhr'] = request.is_xhr
    data['endpoint'] = request.endpoint

    return str(data)

if __name__ == '__main__':
    app.run()
