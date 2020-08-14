###### 字典代替switch case

day = 6

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

# day_name = switcher[day]

day_name = switcher.get(day, 'Unkown')

# 所有的value都是function
# day_name = switcher.get(day, get_default)()

print(day_name)




###### 列表推导式, 集合元组都可以被推导, 只需要把外层的[]改变为{}或者()
print([x**2 for x in range(1, 11)])

# 通过筛选来生成列表
print([x for x in range(1, 11) if x >= 5])

# 使用嵌套来遍历生成
print([x+y for x in 'abc' for y in 'xyz'])

# 列表生成式遍历字典
d = {'a':'1', 'b':'2', 'c':'3', 'd':'4'}
print({v:k for k, v in d.items()})



###### None

'''
None 与 空字符串, 空的列表, 0, False在值和类型都不相等
'''

print(type(None))

# 对象存在不一定是True
class Test():
    def __len__(self):
        return 0

test = Test()

if test:
    print('T')
else:
    print('F')

print(bool(test))
print(bool(None))

# __len__和__bool__都会影响对象的的返回结果
# 执行len()方法的时候也会调用对象中__len__方法


