n ,k = map (int,input().split())
list1 = list(map (int,input().split()))
list1 = sorted(list1,reverse=True)
sum1 = 0
for i in range(k):
    if list1[i] <0:
        break
    sum1 += list1[i]
print(sum1)
