num = int(input()) # 12
result = 0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        result += i
        if i != num**0.5:
            result += num // i
print(result)