import re
# 正则替换
lan = 'PythonC#JavaPHPC#'
# 最后一个参数为最大匹配数, 复杂的替换使用re.sub
# r = re.sub('C#', 'GO', lan, 1)

# 当匹配到时, convert函数会被调用
def convert(value):
    # value是个对象, span为匹配到字符串在源字符串的位置
    matched = value.group()
    return '(' + matched + ')'

r = re.sub('C#', convert, lan)


# r = lan.replace('C#', 'GO')
print(r)



### 找出字符串中的数字然后根据大小作不同的替换

s = 'A8C3721D86'
def convert_num(value):
    matched = value.group()
    return '9' if int(matched) >= 6 else '0'

r = re.sub(r'\d', convert_num, s)

# r = re.sub(r'\d', '-', s)
print(r)
