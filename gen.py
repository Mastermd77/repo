# 1
numbers = [1, 2, 3]
it = iter(numbers)
print(next(it))
print(next(it))

# 2
for num in numbers:
    print(num)

# 3
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

# 4
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# 5
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

# 6
squares = (x*x for x in range(5))
for s in squares:
    print(s)