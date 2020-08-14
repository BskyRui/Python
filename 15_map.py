list_y = [1, 2, 3, 4]

def square(x):
    return x * x

# r是map对象
r = map(square, list_y)
print(list(r))

# map和lambda, 推荐结合在一起使用
r = map(lambda x:x*x, list_y)
print(list(r))


# 传入多个列表
list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 3, 4, 5]
r = map(lambda x, y: x * y, list_a, list_b)
print(list(r))
