# Read input values
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
x = int(input())

# Check if x exists in a
found = False
for i in range(n):
    for j in range(m):
        if a[i][j] == x:
            found = True
            break
    if found:
        break

# Print output
if found:
    print("will not take number")
else:
    print("will take number")

