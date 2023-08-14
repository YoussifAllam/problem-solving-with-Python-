size , result = map(int, input().split())
arr = list(map(int, input().split()))

def check(sum, index):
    if index == size:
        return sum == result
    route1 = check(sum + arr[index], index + 1)
    route2 = check(sum - arr[index], index + 1)
    return route1 or route2

if check(arr[0], 1):
    print("YES")
else:
    print("NO")