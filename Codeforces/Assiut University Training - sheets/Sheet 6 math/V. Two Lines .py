x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

xx1 = x2 - x1
yy1 = y2 - y1

xx2 = x4 - x3
yy2 = y4 - y3

if xx1 * yy2 == xx2 * yy1:
    print("YES")
else:
    print("NO")