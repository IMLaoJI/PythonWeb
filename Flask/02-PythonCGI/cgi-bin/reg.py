import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Info</title>
</head>
<body>
    <table border="1">
        <tr>
            <td>Username</td>
            <td>{user}</td>
        </tr>
        <tr>
            <td>Email</td>
            <td>{email}</td>
        </tr>
        <tr>
            <td>Gender</td>
            <td>{gender}</td>
        </tr>
        <tr>
            <td>City</td>
            <td>{city}</td>
        </tr>
        <tr>
            <td>Agree</td>
            <td>{agree}</td>
        </tr>
        <tr>
            <td></td>
            <td>
                <a href="../reg.html" class="btn btn-default">Back</a>
            </td>
        </tr>
    <table>
</body>
</html>"""

keys = ['user', 'email', 'gender', 'city', 'agree']

data = dict.fromkeys(keys)

data['user'] = form['user'].value
data['email'] = form['email'].value
data['gender'] = form['gender'].value
data['city'] = form['city'].value
data['agree'] = form['agree'].value

print(html.format_map(data))
