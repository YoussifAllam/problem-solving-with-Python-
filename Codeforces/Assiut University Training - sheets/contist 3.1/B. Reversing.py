n = int(input()) 
arr = list(map(int, input().split()))  

for i in range(n):
    if arr[i] == 0:
        arr[:i+1] = arr[:i][::-1] 
        arr.insert(i,0)
        

print(*arr)