import requests

# 创建一个session对象，该对象会自动将请求中的cookie进行存储和携带
session = requests.session()
# 登录请求的url
url = 'https://passport.17k.com/ck/user/login'
# 伪装UA
head_data = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
data = {
    'loginName': '15687117064',
    'password': 'Xzy13398854476@'
}
# 使用session发送请求，目的是为了将session保存该次请求中的cookie
html = session.post(url, headers=head_data, data=data)

# 进行登陆
url = 'https://user.17k.com/www/userinfo/index.html'
head_data = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}
# 再次使用session进行请求的发送，该次请求中已经携带了cookie
html = session.get(url, headers=head_data)
f = open('登陆页面.txt', 'w+', encoding='utf-8')
# 设置响应内容的编码格式
html.encoding = 'utf-8'
# 将响应内容写入文件
f.write(html.text)

