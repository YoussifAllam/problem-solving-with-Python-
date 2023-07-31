n,a,b=map(int,input().split())
sum=0
list1=[]
for i in range(1,n+1):
    sum=0
    #print("i=",i)
    for digit in str(i):
        sum+=int(digit)
    #print("sum=",sum)
    if sum >= a and sum <= b:
        #print("i=",i)
        list1.append(str(i))
sum=0
for i in range(len(list1)):
    sum+=int(list1[i])
print(sum)