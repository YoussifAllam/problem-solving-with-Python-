num1, num2, num3 = map(int, input().split())
ma = max(num1, num2)
mi = min(num1, num2)
result = 1
for i in range(mi, ma + 1):
    result *= i
    result %= num3
print(result)