from django import template

register = template.Library()


# 注册自定义简单标签
@register.simple_tag
def add(strs):
    """加法"""
    strs = strs + strs
    return f'加法{strs}'

@register.simple_tag
def subtract(strs):
    """减法"""
    strs = strs - strs
    return f'减法{strs}'

@register.simple_tag
def ride(strs):
    """乘法"""
    strs = strs * strs
    return f'乘法{strs}'

@register.simple_tag
def division(strs):
    """除法"""
    strs = strs / strs
    return f'除法{strs}'
