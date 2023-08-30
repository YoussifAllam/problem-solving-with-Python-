import math

num1, num2, num3 = map(float, input().split())
if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    sum = num1 + num2 + num3
    print("Valid")
    print(f"{math.sqrt((sum / 2) * (sum / 2 - num1) * (sum / 2 - num2) * (sum / 2 - num3)):.6f}")
else:
    print("Invalid")