n = int(input())
list1 = list(map (int,input().split()))
c = 0
for i in range(n):
    if list1[i] + 1 in list1:
        c+=1
print(c)