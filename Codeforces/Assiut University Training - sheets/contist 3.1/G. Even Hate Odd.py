testCases = int(input())

while testCases > 0:
    size = int(input())
    even = 0
    odd = 0
    arr0 = list( map( int , input().split() ) )
    for i in arr0:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == odd:
        print("0")
    elif size % 2 != 0:
        print("-1")
    else:
        print(abs(even - odd) // 2)
    testCases -= 1