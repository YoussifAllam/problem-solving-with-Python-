n=int(input())
list1=list(input().split())
i=x=total=0
while i < n:
    x=int(list1[i])/100
    total+=x
    i+=1
print((total/n)*100)