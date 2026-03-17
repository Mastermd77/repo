import os
import shutil
from functools import reduce


os.makedirs("a/b/c", exist_ok=True)

print(os.listdir("."))

files = [f for f in os.listdir(".") if f.endswith(".py")]
print(files)






if os.path.exists("test.txt"):
    shutil.move("test.txt", "a/test.txt")
    
    
   

items = [1, 2, 3, 4]

res_map = list(map(lambda x: x + 10, items))
res_filter = list(filter(lambda x: x > 2, items))
res_reduce = reduce(lambda x, y: x + y, items)

print(res_map, res_filter, res_reduce)




names = ["A", "B"]
nums = [1, 2]

for i, name in enumerate(names):
    print(i, name)

for name, n in zip(names, nums):
    print(name, n)

x = "5"
y = int(x)
print(type(x), type(y))