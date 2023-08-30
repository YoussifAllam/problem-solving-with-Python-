line = int(input())
for i in range(line):
    value = 1
    for z in range(i + 1):
        print(value, end=" ")
        value = value * (i - z) // (z + 1)
    print()
