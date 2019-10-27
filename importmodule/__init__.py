# 可以在__init__导入该包下的模块,这些模块的变量和模块就可以通过包来调用了,就是把各个模块的内容传递给了模块.

from .Module1 import *
from .Module2 import *


