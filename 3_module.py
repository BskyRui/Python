# 包(目录) 模块(文件) 类
# 如果想然让一个目录成为一个包的话, 必须在包下面加添一个 __init__.py 文件


# 导入模块
import common.t_import
import common.t_import as alias_name

print(alias_name.a)

# 避免过长的引用名称
from common import t_import
print(t_import.a)

from common.t_import import a 
print(a)

# 可以使用 import *, 在模块中定义 * 的行为 __all__ = ['b', 'c']
from common.t_import import *
# from common.t_import import a, b
print(b, c)
# print(d) name 'd' is not defined

# 每行不超过80个字符(规范), 如果长度超出可以使用()包起来

# __init__.py 的用法，用来控制被 import 的内容
# __init__在被导入的时候会自动运行, 批量导入的时候时候需要在__init__.py文件中定义__all__(模块名)
from common import *
print(p1.name, p2.age, '#####################')
# 如果多个文件需要导入相同的内容, 可以在__init_.py中 import sys, import datetime...

### 1) 包和模块不会被重复的导入
### 2) 避免循环导入

########## 内置变量
infos = dir()
# __name__    __package__    __doc__    __file__

# 绝对引入 一定要从顶级包导入
# 相对引入 python入口文件(main.py)不能使用相对路径导入其它模块




