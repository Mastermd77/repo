#while break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1



a = 0
while a < 10:
    if a == 5:
        break
    print(a)
    a += 1

b = 10
while b > 0:
    print(b)
    if b == 7:
        break
    b -= 1


x = 1
while True:
    print(x)
    if x == 4:
        break
    x += 1

y = 0
while y < 8:
    y += 2
    if y == 6:
        break
    print(y)

k = 5
while k >= 0:
    if k % 2 == 0:
        break
    print(k)
    k -= 1



#while continue 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)




a = 0
while a < 4:
    a += 1
    if a == 2:
        continue
    print(a)

b = 0
while b < 3:
    b += 1
    if b == 1:
        continue
    print(b)


x = 0
while x < 5:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

y = 0
while y < 2:
    y += 1
    continue


k = 0
while k < 3:
    k += 1
    if k == 3:
        continue
    print(k)
