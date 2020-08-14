# 装饰器
import time
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(func.__name__)
        print(time.time())
        func(*args, **kw)
    return wrapper

# 装饰器语法糖
@decorator
def f1(param_one):
    print('This is a function.')


@decorator
def f2(param_one, param_two):
    print('This is a function.')


@decorator
def f3(param_one, param_two, **kw):
    print(f3.__name__)
    print('This is a function.')

#decorator(f1)()

# 被装饰的函数有参数的情况
f3('p1', 'p2', a=1, b=2)

