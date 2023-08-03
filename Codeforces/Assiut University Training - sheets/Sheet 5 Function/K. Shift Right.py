def shift_right(arr, x):
    n = len(arr)
    x = x % n
    return arr[-x:] + arr[:-x]

n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(*shift_right(arr, x))

