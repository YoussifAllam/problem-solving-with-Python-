size, counter = map(int, input().split())

arr = [0] * (counter+1)

num = list(map(int,input().split()))
for i in num:
    arr[i] += 1

for i in range(1, counter + 1):
    print(arr[i])