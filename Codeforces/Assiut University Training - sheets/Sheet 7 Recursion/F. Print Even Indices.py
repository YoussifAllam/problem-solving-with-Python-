n= int(input())
l = list(map(int,input().split()))
len = len(l) 

def recursion(n,l,len):
    if n == 0:
        print(l[n])
    if n >0:
       print(l[n],end= " ")
       recursion(n-2,l,len)


if len %2==0:
   recursion(n-2,l,len)
else:
    recursion(n-1,l,len)
