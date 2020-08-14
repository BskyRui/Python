# 1) for循环外部可以引用for循环内部的变量, python没有块级作用域概念

for x in range(0, 10):
    a = x

print(x)

# 2) 优先使用局部变量(作用域链)

c = 1

def func1():
    # c = 2
    def func2():
        # c = 3
        print(c)
    func2()

func1()

# 3) global, 在整个程序里都可以用(包括另一个模块)

def demo():
    global age
    age = 2

demo()

print(age)