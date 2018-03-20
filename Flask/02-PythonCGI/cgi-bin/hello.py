# 声明网页输出
print('Content-type: text/html\n')

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>优品课堂 Python CGI</title>
</head>
<body>
    <h1>优品课堂 Python CGI</h1>
    <img src="http://temp.im/300x200" alt="">
</body>
</html>"""

print(html)
