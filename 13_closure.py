# 闭包: 函数 + 环境变量(函数定义时外的变量)
def curve_pre():
    a = 10
    def curve(x):
        return a * x * x 
    return curve

# curve_pre函数内部的变量不受影响
a = 20 
# 返回一个闭包
f = curve_pre() 
print(f.__closure__)
print(f.__closure__[0].cell_contents)


# 闭包的经典误区
def f1():
    a = 10
    def f2():
        # a会被认为是局部变量, 闭包是不存在的
        a = 20
        return a
    return f2

f = f1()
print(f.__closure__)


