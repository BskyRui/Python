a = ['a', 2, 3]

# 遍历元素
for k in a:
    print(k)

# 带索引遍历
for k, v in enumerate(a):
    print(k, v)

# 遍历字典
d = {'name': 'lirui', 'age': 22}

for k, v in d.items():
    print(k, v)

# 默认不写变量是key
for k in d:
    print(k)

for k in d.keys():
    print(k)

# 遍历values
for k in d.values():
    print(k)


# 循环

# 0, 9
for x in range(0, 10):
    print(x, end=' | ')

# step
for x in range(0, 10, 2):
    print(x)

# 负数
for x in range(10, 0, -1):
    print(x, end=' | ')
         


