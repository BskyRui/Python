from enum import Enum
# 枚举

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLACK = 4

# 通常关注名称, 这才是枚举的意义而不是数值
print(VIP.GREEN)

# 普通类可变, 值也可以重复, 但枚举类型的值是不能改变, 也不能重复
print(VIP.GREEN.name)
print(VIP.GREEN.value)
# VIP.GREEN
print(VIP['GREEN']) 

# 枚举类型, 枚举的名字, 枚举的值

# 遍历枚举
for v in VIP:
    print(v)

for v in VIP.__members__:
    print(v)  

# 枚举转换
print(VIP(1) == VIP.YELLOW)  

from enum import IntEnum, unique

@unique
class COLOR(IntEnum):
    YELLOW = 1
    GREEN = 2
    # GRAY = 2
    GRAY = 3

print(COLOR)