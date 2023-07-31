num1, num2, num3, num4 = map(int, input().split())
start = 0
end = 0

if (num3 < num1 and num4 < num1) or (num3 > num2 and num4 > num2):
    print(-1)
else:
    start = max(num1, num3)
    end = min(num2, num4)
    print(start, end)