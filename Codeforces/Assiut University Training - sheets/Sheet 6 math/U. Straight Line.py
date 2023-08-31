    x1, y1,  = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    res1 = (y3 - y2) * (x2 - x1)
    res2 = (y2 - y1) * (x3 - x2)

    if res1 == res2:
        print("YES")
    else:
        print("NO")