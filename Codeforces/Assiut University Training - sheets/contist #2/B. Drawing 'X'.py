import sys

counter = int(sys.stdin.readline())

for i in range(counter):
    for z in range(counter):
        if i == z and i != counter//2 and z != counter//2:
            print("\\", end="")
        elif i == counter//2 and z == counter//2:
            print("X", end="")
        elif z != counter//2 and i == (counter-1)-z:
            print("/", end="")
        else:
            print("*", end="")
    print()