# 如何设计类: 行为 和 特征

class Student():
    # 类变量
    sum = 0
    name = ''
    age = 0

    # 构造函数, 只能返回None
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        # 私有变量和方法加__, _Student__score
        self.__score = 60;
        # 调用父类构造函数
        # super(Student, self).__init__(name, age)
    
    def print_info(self):
        print(self.name, self.age)

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
    
    # 静态方法, 不要常使用
    @staticmethod
    def add(x, y):
        pass


student = Student('lirui', 18)
# 调用类下面的方法
student.print_info()
# 类变量和实例变量的区别
print(student.name, Student.sum)
# 类变量的意义: 比如在类变量中定义一个 sum = 0, 先查找是否有实例变量, 如果不存在则会去类变量列表查找

# 调用类方法, 不要用实例变量去调用类方法
Student.plus_sum()

# print(student.__score);



