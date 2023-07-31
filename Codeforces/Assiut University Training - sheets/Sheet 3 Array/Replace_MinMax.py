n=int(input())
list1=list(map(int,input().split()))
def getminpos(list2):
    Min=list2[0]
    p1=0
    for i in range(n):
        if Min>list2[i]:
            Min=list2[i]
            p1=i
    return p1

def getmaxpos(list2):
    Max=list2[0]
    p2=0
    for i in range(n):
        if Max<list2[i]:
            Max=list2[i]
            p2=i
    return p2

pos1=getminpos(list1)
pos2=getmaxpos(list1)

temp=list1[pos1]
list1[pos1]=list1[pos2]
list1[pos2]=temp

for i in range(n):
 print(list1[i],end=" ")
 