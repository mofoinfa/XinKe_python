def add(a, b):
    """加"""
    return a + b


def delete(a, b):
    """减"""
    return a - b


def ride(a, b):
    """乘"""
    return a * b


def divide(a, b):
    """除"""
    return a / b


def exact_division(a, b):
    """是否能被整除"""
    return True if a % b == 0 else False


def odevity(data):
    """判断是否是奇偶数"""
    return 1 if data % 2 != 0 else 2


