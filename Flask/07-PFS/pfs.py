# pfs : problem feedback system
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

conn = sqlite3.connect(r'./db/feedback.db')
c = conn.cursor()

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/feedback/')
def feedback():
    sql = 'select ROWID,CategoryName from category'
    categories = c.execute(sql).fetchall()
    return render_template('post.html', categories=categories)

if __name__ == '__main__':
    app.run()
