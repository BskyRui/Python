# 过滤到不符合规则的元素

list_x = [1, 2, 3, 4, 5, 6]

# 根据函数的返回值
r = filter(lambda x: True if x % 2 == 0 else False, list_x)

print(list(r))