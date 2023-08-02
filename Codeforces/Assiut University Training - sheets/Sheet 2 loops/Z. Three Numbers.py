start, end = map(int, input().split())

counter = 0

for i in range(start + 1):
    for z in range(start + 1):
        if end - i - z >= 0 and end - i - z <= start:
            counter += 1

print(counter)