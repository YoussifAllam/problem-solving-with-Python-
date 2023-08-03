from decimal import Decimal
num1, num2, num3 = map(Decimal, input().split())
result = (num1 * num2) / num3
myNumber = int(result)
myRes = result - myNumber
if myRes > 0:
    print("double")
elif myNumber <= 2147483647:
    print("int")
else:
    print("long long")