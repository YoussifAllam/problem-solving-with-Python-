row, column = map(int, input().split())

arr = [[""] * 101 for _ in range(101)]

for i in range(1, row + 1):
    line = input()
    for z in range(1, column + 1):
        arr[i][z] = line[z - 1]

rowIn, columnIn = map(int, input().split())

if (arr[rowIn][columnIn - 1] != '.' and
    arr[rowIn][columnIn + 1] != '.' and
    arr[rowIn - 1][columnIn] != '.' and
    arr[rowIn + 1][columnIn] != '.' and
    arr[rowIn - 1][columnIn - 1] != '.' and
    arr[rowIn - 1][columnIn + 1] != '.' and
    arr[rowIn + 1][columnIn - 1] != '.' and
    arr[rowIn + 1][columnIn + 1] != '.'):
    print("yes")
else:
    print("no")