a,b=map(int,input().split())
i=t=1
list1=[]
list2=[]
def check(number :int,list3):
    i=1
    for i in range(1, number+1):
     if number % i == 0:
        list3.append(i)
     i+=1

check(a,list1)
check(b,list2)

list1.sort()
list2.sort()


j=len(list1)-1

while j > -1:
    j2=len(list2)-1

    while j2 > -1:
     if list1[j]==list2[j2]:
        print( list1[j])
        t=0
        break
     j2-=1
    if t==0:
        break
    j-=1

