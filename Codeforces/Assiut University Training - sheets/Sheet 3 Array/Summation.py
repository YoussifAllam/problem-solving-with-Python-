n=int(input())
sum=0
list1=list(input().split())
list1=[int(i) for i in list1]

for i in range(n):
    sum+=list1[i]
print(abs(sum))
