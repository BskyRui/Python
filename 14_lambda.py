# 匿名函数
l = lambda x: 2 * x
print(l(2))

l2 = lambda x, y: x * y

print(l2(2, 3))

# def是语句, lambda是表达式
l = [(lambda x: x * x)(x) for x in range(1, 22)]
print(l)