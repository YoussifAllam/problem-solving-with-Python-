import sys 
counter = int(input()) 
while counter > 0:
    size = int(input()) 
    arr = list(map(int, input().split())) 
    for x in arr: 
        print(x, end=" ")
    i = 0 
    z = 0 
    ma = -sys.maxsize 
    while True: 
        if z == size - 1:
            break 
        if i == z: 
            ma = max(arr[i], arr[i+1]) 
        else: 
            ma = max(ma, arr[i+1]) 
        print(ma, end=" ")
        i += 1 
        if i == size - 1: 
            z += 1 
            i = z 
    print() 
    counter -= 1 