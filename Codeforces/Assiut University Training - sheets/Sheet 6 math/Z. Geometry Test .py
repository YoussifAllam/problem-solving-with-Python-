import math

r, s = map(int, input().split())

if s >= r * 2:
    print("Square")
elif r * 2 > math.sqrt(s ** 2 + s ** 2):
    print("Circle")
else:
    print("Complex")