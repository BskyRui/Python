import json
# json是一种数据格式, 字符串是json的表现形式(载体), 符合json格式的字符串就叫json字符串

# string
json_str = '{"name": "lirui", "age": 22}'
# array
json_info = '[{"name": "lirui", "age": 22}, {"name": "LIRUI", "age": 23}]'

# info = json.loads(json_str)

# print(type(info))
# print(info['name'])

# 字符串到内置类型(反序列化)
info = json.loads(json_info)
print(info)

# 序列化
'''
json -> python
object dict
array  list
string str
number int
number float
true   True
false  False
null   None
'''

d = [{'name': 'lirui', 'age': 23}, {'name': 'Lr', 'age': 23}]
json_str = json.dumps(d)
print(json_str)
