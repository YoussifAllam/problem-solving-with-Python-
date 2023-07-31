n=int(input())
list1=list(input().split())
list1=[int(i) for i in list1]
for i in range(n):
    if list1[i]<=10:
        print("A[",i,"] = ",list1[i],sep="")
