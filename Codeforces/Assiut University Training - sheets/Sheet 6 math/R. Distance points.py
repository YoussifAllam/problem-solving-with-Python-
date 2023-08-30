x1, y1, x2, y2 = map(float, input().split())
d1 = x1 - x2
d2 = y1 - y2
result = ((d1 ** 2) + (d2 ** 2)) ** 0.5
print(f"{result:.9f}")