from flask import request, session, make_response, redirect, url_for, render_template

def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return "用户中心"

def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    return "个人资料页"

def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        pwd = request.form.get('pwd', None)
        
