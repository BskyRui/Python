# re.search, re.match没有findall好用

import re

s = '83C72D1D8E67';
# 尝试从字符串的 首字母 匹配
r = re.match('\d', s)
print(r.span())

# 搜索整个字符串, 返回第一个匹配成功的
r1 = re.search('\d', s)
print(r1)

# match和search返回的是一个对象, 而findall返回的是list, match和search都只会匹配一次
print(r1.group())