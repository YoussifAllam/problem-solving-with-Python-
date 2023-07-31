counter = int(input())
while counter > 0:
    size = int(input())
    result = 0
    arr = list(map(int, input().split()))
    result = size
    i = 0
    z = 0
    while True:
        if z == size - 1:
            break
        if arr[i] > arr[i+1]:
            z += 1
            i = z
            continue
        result += 1
        i += 1
        if i == size - 1:
            z += 1
            i = z
    print(result)
    counter -= 1