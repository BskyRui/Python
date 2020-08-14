# 1) 必须参数
def add(x, y):
    return x + y

print(add(1, 2))

# 2) 关键字参数
print(add(y=3, x=3))

# 必须参数和关键字参数的区别就是函数在调用的方式不一样

# 3) 默认参数

def sum(x=1, y=3):
    return x + y

print(sum(x=5), sum(2, 2), sum(3))

# 4) 可变参数, 如果有必须参数的话, 必须参数必须在可变参数的前面
def func(*param):
    # tuple
    print(param)

func(1, 2, 3)
a = (3, 5, 4)
func(*a)

def squsum(*param):
    sum = 0
    for i in param:
        sum += i*i
    print(sum)


# 5) 任意个数的关键字参数
def info(**data):
    for k, v in data.items():
        print(k, v)
data = {'name': 'lr', 'age': 22}    
info(**data)

 