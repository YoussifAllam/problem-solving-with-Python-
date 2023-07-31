n=int(input())
list1=list(input().split())
list2=[]
i=len(list1)-1
while i >-1:
    list2.append(list1[i])
    i-=1
print(" ".join(list2))