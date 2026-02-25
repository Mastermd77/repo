import math
import random

# 1
print(min(3, 7, 2))
print(max(3, 7, 2))

# 2
print(abs(-10))

# 3
print(round(3.14159, 2))

# 4
print(pow(2, 3))

# 5
print(math.sqrt(16))
print(math.ceil(4.3))
print(math.floor(4.7))
print(math.pi)
print(math.e)

# 6
print(random.random())
print(random.randint(1, 10))

list1 = ["apple", "banana", "cherry"]
print(random.choice(list1))
random.shuffle(list1)
print(list1)