
num1 , num2 = map(int,input().split())


if num1 == 0 and num2 == 0 or abs(num1 - num2) >= 2:
    print("NO")
else:
    print("YES")
