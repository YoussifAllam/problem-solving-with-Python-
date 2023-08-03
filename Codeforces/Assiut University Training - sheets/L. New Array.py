def concatenate_arrays(a, b):
    return b + a

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = concatenate_arrays(a, b)

print(*c)