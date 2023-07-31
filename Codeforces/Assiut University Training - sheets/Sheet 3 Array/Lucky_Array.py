n=int(input())
list1=list(map(int,input().split()))
m=min(list1)
frequency =list1.count(m)
if frequency %2 !=0:
    print("Lucky")
else:
    print("Unlucky")
