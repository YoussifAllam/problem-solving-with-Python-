
size = int(input())
while size > 0:
    num1, num2 = map(int, input().split())
    ma = max(num1, num2)
    mi = min(num1, num2) - 1
    result1 = mi * (mi + 1) // 2
    result2 = ma * (ma + 1) // 2
    print(result2 - result1)
    size -= 1