# utf8 只读方式打开
fd = open('./0_in_output.py', 'r', encoding='utf8')

print(fd.read())

# 关闭
fd.close()


# 推荐写法
with open('./0_in_output.py', 'r', encoding='utf8') as fd:
    data = fd.read()

print(data)     

# 不需要 close