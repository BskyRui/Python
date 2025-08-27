# 整型和浮点型
# int
print(type(1))
print(type(1.1))
# float
print(type(1 + 1.0))
# float
print(type(1 * 1.0))
# float 
print(type(2 / 2))
# int 
print(type(2 // 2))
# 整除, 0
print(1 // 2, 1 / 2)


print("swap a, b")
a = 2
b = 3
a, b = b, a
print(a, b)

############### 进制 ###################

# 进制
# 二进制 3
print(0b11)
# 八进制 9
print(0o11)
# 十六进制 16 + 15 = 31
print(0x1f)

# 其他进制转换为 二进制
# 0b10
print(bin(2))
# 0b11
print(bin(0x03))
# 0b111
print(bin(0o7))
# 其他进制转换为 十进制
# 2
print(int(0b10))
# 9
print(int(0o11))
# 31
print(int(0x1f))

# 其他进制转换为 十六进制
# 0x20
print(hex(32))
# 0x7
print(hex(0b111))
# 0x9
print(hex(0o11))

# 其他进制转换为 八进制
print(oct(0b111))
print(oct(0x1f))

############### 数据类型 ###################

# 布尔类型(Number)
print(int(True))
print(int(False))
print(bool(''))
print(bool(0))
print(bool(None))

print("string---------------------------")
# 字符串
tip = '''
    hello,
    world'''
print(tip)
print('hello, \\n world.')
# 原始字符串
print(r'hello, \n world.')
# 字符串截取
print('hello,world.'[-1:], 'hello,world.'[-1])

# 截取hello
print('hello,world.'[0:5])
print('hello,world'[:5])
print('hello,world.'[:-7])
# hello,world
print('hello,world.'[0:-1])
# 从指定到位置截取到末尾
print('hello,world.'[6:])
print('hello,world.'[-6:])
print('hello,world.'[:-7])


############### 序列 ###################
print('############# list ###############')

# list(嵌套列表 == 二维数组)
print(type([1, 2, 3, '4']))
# 如果用索引的方式去取列表的元素会返回元素的实际类型, 但如果用切片的方式会返回一个新列表
arr = ['li', 'rui']
print(type(arr[-1:]))
print(arr[-1:])
# 两个列表可以用 + 来生成新的列表, str / list / tuple 被称之为序列

# 拆包
arr1, arr2 = ["L", "R"]
print(f'unpack=> arr1={arr1} arr2={arr2}')

print('############# tuple ###############')
# tuple和list对比, 元组不能被修改, 当只有一个元素的时候需要加上逗号(1, )

print(3 in [3, 2])
# 3是否不在list中
print(3 not in [3, 2])
# 列表的长度
print(len([1, 3]))
# 最大的元素
print(max([1, 3, 9, 8]))
# 得到asiic码 
print(ord('a'))


print('############# set ###############')
# set集合, 无序 / 不重复   
s = {1, 2, 3, 4}
print(len(s), 1 in s)
# 求两个集合的差集
print(s - {1, 2})
# 求两个集合的交集
print(s & {3, 4})
# 求两个集合的并集
print(s | {3, 4, 5})
# 定义空的集合
empty_s = set()

# dict字典(不属于序列)
# key不一定是字符串, 还可以是字符串, 但key是不可变的类型

'''
    int str tuple(不可改变, 值类型), list set dict(可变, 引用类型)
    关系运算 == 比较的是两个变量的值, is比较的是两个变量的内存(身份)地址是否相等
'''

