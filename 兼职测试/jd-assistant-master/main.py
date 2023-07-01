#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from configparser import ConfigParser
import os


def initialize_msg():
    """输入对应的信息"""
    print('提示：加入购物车后，输入对应信息自动进行抢单和购买')
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
    cf = ConfigParser()

    cf.add_section('account')
    password = input('请输入支付密码：')
    cf.set('account', 'payment_pwd', password)

    cf.add_section('config')
    eid = input('请输入eid：')
    fp = input('请输入fp：')
    track_id = input('请输入track_id：')
    risk_control = input('请输入risk_control：')
    cf.set('config', 'eid', eid)
    cf.set('config', 'fp', fp)
    cf.set('config', 'track_id', track_id)
    cf.set('config', 'risk_control', risk_control)
    cf.set('config', 'timeout', '10')
    cf.set('config', 'random_useragent', 'false')

    cf.add_section('messenger')
    cf.set('messenger', 'enable', 'false')
    cf.set('messenger', 'sckey', '')

    cf.write(open(file_path, 'w'))


if __name__ == '__main__':
    initialize_msg()
    sku_ids = '100001324422'  # 商品id
    area = '1_72_4211'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
