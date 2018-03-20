from flask import Flask

app = Flask(__name__)  # 根路径指定为hello.py的位置
# app.debug = True

@app.route('/')
def index():
    return 'Hello 优品课堂'    

if __name__ == '__main__':
    app.run(debug=True)
