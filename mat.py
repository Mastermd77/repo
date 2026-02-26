import math

deg = float(input())
rad = deg * math.pi / 180
print(f"{rad:.6f}")

h = float(input())
b1 = float(input())
b2 = float(input())
area_trap = (b1 + b2) * h / 2
print(area_trap)

sides = int(input())
length = float(input())
area_poly = sides * length ** 2 / (4 * math.tan(math.pi / sides))
print(area_poly)

base = float(input())
height = float(input())
area_para = base * height
print(area_para)