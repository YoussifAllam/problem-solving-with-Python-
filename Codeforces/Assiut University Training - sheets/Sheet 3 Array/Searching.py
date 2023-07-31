n=int(input())
t=0
list1=list(input().split())
list1=[int(i) for i in list1]
b=int(input())

for i in range(n):
    if list1[i] == b:
        t=1
        print(i)
        break
if t!=1:
    print(-1)

