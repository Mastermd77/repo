#for loop
for x in range(6):
    print(x)




for a in [10, 20, 30]:
    print(a)

for b in "hello":
    print(b)

nums = [1, 3, 5]
for n in nums:
    print(n * 2)

for i in range(2, 7, 2):
    print(i)


data = {"x": 1, "y": 2}
for k in data:
    print(k, data[k])

#for loop with break
for x in range(6):
    if x == 3:
        break
    print(x)



for a in [1, 2, 3, 4]:
    if a == 3:
        break
    print(a)

for b in "python":
    if b == "h":
        break
    print(b)

nums = [5, 7, 9, 11]
for n in nums:
    if n > 8:
        break
    print(n)
    
    

for i in range(10, 0, -1):
    if i == 6:
        break
    print(i)
    
    
    
#for loop with continue
for x in range(6):
    if x == 3:
        continue
    print(x)



for a in [1, 2, 3, 4]:
    if a == 2:
        continue
    print(a)
    
    
    
    
    

for b in "world":
    if b == "o":
        continue
    print(b)

nums = [2, 4, 5, 7]
for n in nums:
    if n % 2 == 0:
        continue
    print(n)
    

for i in range(5):
    if i < 2:
        continue
    print(i)
