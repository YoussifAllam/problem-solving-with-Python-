def GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def LCM(num1, num2):
    return (num1 // GCD(num1, num2)) * num2

num1, num2 = map(int, input().split())
print(GCD(num1, num2), LCM(num1, num2))