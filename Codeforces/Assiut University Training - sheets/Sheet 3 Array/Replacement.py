n=int(input())
list1=list(input().split())
list1=[int(i) for i in list1]
for i in range(n):
    if list1[i]<0:
        list1[i]=2
    elif list1[i]>0:
        list1[i]=1
for i in range(n):
    print(list1[i],end=" ")
