import math

xAxes = [0] * 1000
yAxes = [0] * 1000

x, y, nq, points = map(int, input().split())

for i in range(points):
    xAxes[i], yAxes[i] = map(int, input().split())

for i in range(points):
    x1 = x - xAxes[i]
    y1 = y - yAxes[i]
    result = math.sqrt(x1 ** 2 + y1 ** 2)
    if result > nq:
        print("NO")
    else:
        print("YES")