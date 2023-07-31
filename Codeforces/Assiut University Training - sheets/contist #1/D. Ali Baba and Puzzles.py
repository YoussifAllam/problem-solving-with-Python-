num1, num2, num3, result = map(int, input().split())

flag = 0

myResult1 = (num1 * num2) - num3
myResult2 = (num1 * num2) + num3
myResult3 = num1 + (num2 * num3)
myResult4 = num1 - (num2 * num3)
myResult5 = (num1 - num2) + num3
myResult6 = (num1 + num2) - num3

if myResult1 == result or myResult2 == result or myResult3 == result or myResult4 == result or myResult5 == result or myResult6 == result:
    flag = 1

if flag == 1:
    print("YES")
else:
    print("NO")