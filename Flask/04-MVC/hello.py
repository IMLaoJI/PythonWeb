from flask import Flask, render_template
from models.book import Book

app = Flask(__name__)  # 根路径指定为hello.py的位置
# app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books/')
def book_list():
    books = [
        Book('Python Flask', 59.00, 'Eason', '人民邮电出版社'),
        Book('Python Selenium', 59.00, 'Tom', '人民邮电出版社'),
        Book('Python 爬虫', 39.00, 'Eason', '北京大学出版社'),
        Book('Python 多线程', 49.00, 'Eason', '清华大学出版社'),
        Book('Python 语言', 29.00, 'Eason', '人民邮电出版社')
    ]
    return render_template('book-list.html', books=books)


@app.route('/contact/')
def contact():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
    </head>
    <body>
        <h1>联系我们</h1>
    </body>
    </html>"""
    return html


if __name__ == '__main__':
    app.run(debug=True)
