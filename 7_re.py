import re

string = 'PHP0Python9C++0C8JavaScript'

r = re.findall(r'\d', string)

print(r)

##### 字符集 #####

# \d 这类就叫元字符

string = 'abc, acc, adc, aec, afc, ahc'

# 找到acc或afc
r = re.findall('a[cf]c', string)
print(r)

# 找到非acc和afc
r = re.findall('a[^cf]c', string)
print(r)

# 找到acc, adc, aec, afc
r = re.findall('a[c-f]c', string)
print(r)


##### 概括字符集 #####
# 只能匹配单一字符
# \d 
# \D (非数字) 
# \w (单词字符, a-zA-Z0-9_)  
# \W 非单词字符 
# \s 空白字符 
# \S 非空白字符
# . 匹配除换行符\n之外的所有字符

string = 'python111java123&php333\t\n'

r = re.findall(r'\w', string)
print(r)


##### 数量词 #####

string = 'python111java123&php333'

r = re.findall('[a-z]{3,6}', string)
print(r)

# 贪婪和非贪婪, python倾向于贪婪, 尽可能的匹配更多

# * 匹配0次或者无线多次
# + 匹配1次或者无线多次
# ? 0或者1次
string = 'pytho0python1pythonn2'

r = re.findall('python?', string)  # ['pytho', 'python', 'python']

# ?在这里代表非贪婪模式,只匹配一个 n
r = re.findall('python{1,2}?', string)
print(r)


##### 边界匹配 #####
qq = '100000001'
# ^字符串开头, $字符串结尾
r = re.findall('^\d{4,8}$', string)
print(r)


##### 组 #####
string = 'PythonPythonPython1'
# 小括号是且的关系，3个 Python
r = re.findall('(Python){3}', string)
print('group', r)


##### 匹配模式 ######

lan = 'PythonC#\nJavaPHP'
# r = re.findall('c#.{1}', lan, re.I )
# re.S 使.匹配支持换行符
r = re.findall('c#.{1}', lan, re.I | re.S)
print(r)