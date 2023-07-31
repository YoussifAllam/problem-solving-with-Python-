list1=list(map(int,input().split()))
list2=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print(len(list1)-len(list2))
