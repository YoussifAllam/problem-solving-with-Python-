sum =k=0
t=int(input())
while k<t:
    sum=0
    a,b=map(int,input().split())

    if b>a:
            for i in range(a+1,b):
                if int(i)%2!=0:
                   sum+=int(i)
            print(sum)
    else:
            for i in range(b+1,a):
               if int(i)%2!=0:
                   sum+=int(i)
            print(sum)
    k+=1

