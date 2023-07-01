user_msg = {
    '小王': {'username': '123456', 'password': '123456'},
    '小明': {'username': '1234567', 'password': '1234567'}
}
is_login = False


def input_log(user_msg, func):
    """输入登陆信息"""
    global is_login
    print('-' * 10, '登陆页面', '-' * 10)
    username = input('请输入账号:')
    password = input('请输入密码:')
    for i in user_msg:
        if username == user_msg[str(i)]['username'] and password == user_msg[str(i)]['password']:
            is_login = True
    if is_login:
        print('-' * 20)
        func()
        print('-' * 20)
    else:
        print('账号密码错误或未输入')


def func(f):
    """装饰器"""

    def inter():
        global is_login
        if is_login:
            print('-' * 20)
            f()
            print('-' * 20)
        else:
            input_log(user_msg, f)

    return inter


@func
def add_msg():
    """增加用户信息"""
    name = input('输入用户名字：')
    username = input('请输入账号:')
    password = input('请输入密码:')
    user_msg[name] = {'username': username, 'password': password}
    print('用户信息增加成功！')


@func
def del_msg():
    """删除用户信息"""
    name = input('请输入删除用户名称：')
    del user_msg[name]
    print('用户信息删除成功！')


@func
def change_msg():
    """更改用户信息"""
    name = input('请输入更改用户名称：')
    for i in user_msg:
        if i == name:
            username = input('请输入更改用户账号：')
            password = input('请输入更改用户密码：')
            user_msg[name] = {'username': username, 'password': password}
            print('用户信息更改成功！')
            return
    print('未找到此用户')


@func
def select_msg():
    """查询用户信心"""
    for i in user_msg:
        print(f"名称：{i}  账号：{user_msg[i]['username']} 密码：{user_msg[i]['password']}")


while True:
    num = input('1：增加\n2：删除\n3：更改\n4：查询\n5：退出\n请输入标号选择服务:')
    if num == '1':
        add_msg()
    elif num == '2':
        del_msg()
    elif num == '3':
        change_msg()
    elif num == '4':
        select_msg()
    elif num == '5':
        break
    else:
        print('无此服务')
