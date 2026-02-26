def gen1(n):
    for i in range(n + 1):
        yield i ** 2

def gen2(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def gen3(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def gen4(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def gen5(n):
    for i in range(n, -1, -1):
        yield i

n1 = int(input())
for i in gen1(n1):
    print(i)

n2 = int(input())
for i in gen2(n2):
    print(i, end=",")
print()

n3 = int(input())
for i in gen3(n3):
    print(i)

a4 = int(input())
b4 = int(input())
for i in gen4(a4, b4):
    print(i)

n5 = int(input())
for i in gen5(n5):
    print(i)