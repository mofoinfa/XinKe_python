# 商品管理系统

def choose_desigh():
    """选择页面初始化"""
    print('-' * 10, '小熊商城', '-' * 10)
    print('1.注册', '2.登陆', '3.退出系统')
    choose_type = int(input('请输入选择的服务(输入对应编号):'))
    if choose_type == 1:
        register_role()
        return True
    elif choose_type == 2:
        nickname, role = login_role()
        if role == '用户':
            store_desigh(nickname)
        elif role == '开发者':
            develop_desigh(nickname)
        else:
            print('没有此账号')
        return True
    else:
        return False


def store_desigh(nickname):
    """商品页面初始化"""
    juage_end = True
    print(f'欢迎用户{nickname}进入小熊商城')
    select_goods('用户')
    while juage_end:
        print('1.查看商品', '2.购买商品', '3.查找商品', '4.返回主页面')
        choose_type = int(input('请输入选择的服务(输入对应编号):'))
        if choose_type == 1:
            select_goods('用户')
        elif choose_type == 2:
            sell_goods()
        elif choose_type == 3:
            select_good()
        else:
            break


def develop_desigh(nickname):
    """开发者页面初始化"""
    juage_end = True
    print(f'欢迎开发者{nickname}进入')
    select_goods('开发者')
    while juage_end:
        print('1.查看商品', '2.添加商品', '3.修改商品', '4.返回主页面')
        choose_type = int(input('请输入选择的服务(输入对应编号):'))
        if choose_type == 1:
            select_goods('开发者')
        elif choose_type == 2:
            add_goods()
        elif choose_type == 3:
            update_goods()
        else:
            break


def add_goods():
    """添加商品"""
    name = input('请输入商品名:')
    if name in goods:
        print('商品已经存在！')
    else:
        price = int(input('请输入商品价格:'))
        count = int(input('请输入商品库存:'))
        goods[name] = {'price': price, 'count': count, 'sell_num': 0}


def update_goods():
    """修改商品"""
    name = input('请输入商品名:')
    if name not in goods:
        print('未找到该商品!')
    else:
        price = int(input('请重新输入商品价格:'))
        count = int(input('请重新输入商品库存:'))
        sell_num = int(input('请重新输入商品销售量:'))
        goods[name] = {'price': price, 'count': count, 'sell_num': sell_num}


def sell_goods():
    """出售商品"""
    goods_name = input('请输入购买商品名称：')
    if goods[goods_name]['count'] == 0:
        print('此商品已经售光!')
    else:
        goods[goods_name]['count'] -= 1
        goods[goods_name]['sell_num'] += 1
        print('购买成功!')


def select_good():
    """查看单个商品"""
    try:
        name = input('请输入商品名称：')
        if goods[name]['count'] <= 0:
            print('此商品不存在')
        else:
            print('-' * 24)
            print(f'商品名：{name}')
            print(f'价格：{goods[name]["price"]}')
            print(f'库存：{goods[name]["count"]}')
            print('-' * 24)
    except:
        print('此商品不存在')


def select_goods(user):
    """查看多个商品"""
    t = 1  # 计数器
    if user == '用户':
        print('-' * 10, '货架', '-' * 10)
        for name in goods.keys():
            # print(goods[name])
            if goods[name]['count'] <= 0:
                continue
            else:
                print(name, end=' ')
                if t % 5 == 0:
                    print()
                t += 1
        print('\n', '-' * 24)
    else:
        print('-' * 24)
        print('商品名', '价格', '库存', '销量', sep='\t')
        for name in goods.keys():
            if len(name) < 3:
                print(name, ' ', goods[name]['price'], goods[name]['count'], goods[name]['sell_num'], sep='\t')
            else:
                print(name, goods[name]['price'], goods[name]['count'], goods[name]['sell_num'], sep='\t')
        print('-' * 24)


def login_role():
    """登陆判断"""
    username = input('请输入账号:')
    password = input('请输入密码:')
    try:
        if role_user[username]['password'] == password:
            return role_user[username]['nickname'], role_user[username]['role']
        else:
            return False, False
    except:
        return False, False


def register_role():
    """注册"""
    nickname = input('请输入昵称:')
    username = input('请输入账号:')
    password = input('请输入密码:')
    role_user[username] = {'nickname': nickname, 'password': password, 'role': '用户'}
    print('注册成功')


juage_end = True

role_user = {'1': {'nickname': '小明', 'password': '1', 'role': '用户'},
             '2': {'nickname': '小王', 'password': '2', 'role': '开发者'}
             }
goods = {'土豆片': {'price': 2, 'count': 1, 'sell_num': 0},
         '牙膏': {'price': 10, 'count': 0, 'sell_num': 0},
         '毛巾': {'price': 5, 'count': 100, 'sell_num': 0},
         '苹果': {'price': 5, 'count': 100, 'sell_num': 0},
         '矿泉水': {'price': 2, 'count': 100, 'sell_num': 0},
         '扑克牌': {'price': 2, 'count': 100, 'sell_num': 0}}
while juage_end:
    juage_end = True if choose_desigh() else False

