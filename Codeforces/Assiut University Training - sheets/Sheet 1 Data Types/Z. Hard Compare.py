import math

num1, num2, num3, num4 = map(float, input().split())

res1 = num2 * math.log(num1)

res2 = num4 * math.log(num3)

if res1 > res2:
    print("YES")
else:
    print("NO")