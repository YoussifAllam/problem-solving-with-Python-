from math import sqrt
x1, y1, x2, y2 = map(float, input().split())
x3, y3, x4, y4 = map(float, input().split())
midX1 = (x1 + x2) / 2
midy1 = (y1 + y2) / 2
midX2 = (x3 + x4) / 2
midy2 = (y3 + y4) / 2

r1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 2
r2 = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2) / 2

line = sqrt((midX1 - midX2) ** 2 + (midy1 - midy2) ** 2)
rr = r1 + r2

if line > rr:
    print("NO")
else:
    print("YES")