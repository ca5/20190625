import module001
import module002
import module002.hoge
from module002 import hoge

print(module001.module001_function001())
print(module002.module002_init_function())
print(module002.hoge.module002_hoge_function())
print(hoge.module002_hoge_function())