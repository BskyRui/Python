import re

s = 'life is short, i use python, i love python'

# 默认会把整体匹配到的字符串当作一个分组
r = re.search('life(.*)python(.*)python', s)

print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(0, 1, 2))
print(r.groups())