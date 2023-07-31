n=int(input())
list1=list(input().split())
list1=[int(i) for i in list1]
min=list1[0]
pos=0
for i in range(n):
    if list1[i]<min:
        min=list1[i]
        pos=i
print(min,pos+1)
