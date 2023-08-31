x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

mi_x = min(min(x1, x2), min(x3, x4))
ma_x = max(max(x1, x2), max(x3, x4))
mi_y = min(min(y1, y2), min(y3, y4))
ma_y = max(max(y1, y2), max(y3, y4))

points = int(input())

for i in range(points):
    x, y = map(int, input().split())
    if mi_x <= x <= ma_x and mi_y <= y <= ma_y:
        print("YES")
    else:
        print("NO")