url = 'http://ke.qq.com'
import urllib.request
d = {'id':123918, 'name':'Tom'}
import urllib.parse
params = urllib.parse.urlencode(d)
print(params)
# req = urllib.request.Request(url, method='GET', params=params)
rsp = urllib.request.urlopen(f'{url}?{params}')
rsp.read()

req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")



rsp.status
rsp.getcode()
rsp.geturl()
rsp.reason
rsp.info()
d = dict(rsp.info())
print(d)
b = rsp.read()
print(b)
html = b.decode()  # 不填则默认使用utf8解码
print(html)
