N = int(input())
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    for a in range(2 * i - 1):
        print("*", end="")

    print()


for i in range(N , 0, -1):
    for j in range(N - i):
        print(" ", end="")
    for a in range(2 * i - 1):
        print("*", end="")

    print()