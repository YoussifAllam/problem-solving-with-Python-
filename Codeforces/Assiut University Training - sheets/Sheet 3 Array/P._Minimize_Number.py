n = int(input())
a = list(map(int, input().split()))

max_ops = 0
while all(x % 2 == 0 for x in a):
    max_ops += 1
    a = [x // 2 for x in a]

print(max_ops)
