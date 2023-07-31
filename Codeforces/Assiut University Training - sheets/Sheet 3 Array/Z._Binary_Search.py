def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False



n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort()


for i in range(q):
    x = int(input())
    if binary_search(a, x):
        print("found")
    else:
        print("not found")
