sum =0
while True:
    sum=0
    a,b=map(int,input().split())
    if a <=0 or b<=0:
        break
    else:
        if b>a:
            for i in range(a,b+1):
               sum+=int(i)
               print(i,end=" ")
            print("sum =",sum,sep="")
        else:
            for i in range(b,a+1):
               sum+=int(i)
               print(i,end=" ")
            print("sum =",sum,sep="")
