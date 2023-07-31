num1, num2, num3, num4 = map(int, input().split())
 
newNum1 = num1 % 100
newNum2 = num2 % 100
newNum3 = num3 % 100
newNum4 = num4 % 100
 
result = (newNum1 * newNum2 * newNum3 * newNum4)
 
lastTwoDigits = result % 100
 
if lastTwoDigits <= 9:
    print("0" + str(lastTwoDigits))
else:
 
    print(lastTwoDigits)