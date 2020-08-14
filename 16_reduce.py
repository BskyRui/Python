from functools import reduce

list_x = [1, 2, 3, 4, 5, 6]

# 连续计算, 连续调用, 第1次调用的时候会取第0和第1个元素作为lambda表示的参数, 第2次调用时x为上次lambda返回的结果(3), y为3(第2个元素)
# 每次遍历lambda的计算结果作为x的参数再次参与计算
# initial设置第一次的初始值
r = reduce(lambda x,y:x+y, list_x, 10) 

print(r)