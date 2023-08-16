def sum(n):
    return n * (n + 1) // 2

num1, num2, c = map(int, input().split())
ma = max(num1, num2)
mi = min(num1, num2)
print((sum(ma // c) * c) - (sum((mi - 1) // c) * c))