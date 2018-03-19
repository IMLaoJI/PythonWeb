import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')

# name = 'unknow'
# if 'user' in form:
#     name = form['user'].value

name = form['user'].value if 'user' in form else 'unknow'

print('<h1>Hello {}</h1>'.format(name))

