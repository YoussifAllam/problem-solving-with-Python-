n = int(input())

x = 0
y = 0

for i in range(1, 10**9 + 1):
    for j in range(1, 10**9 + 1):
        if (i**2 + j**2) % n == 0:
            x = i
            y = j
            break
    if x != 0 and y != 0:
        break

if x != 0 and y != 0:
    print(x, y)
else:
    print("No solutions")
    