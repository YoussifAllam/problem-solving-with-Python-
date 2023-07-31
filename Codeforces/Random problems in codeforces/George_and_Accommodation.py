n=int(input())
c=0
for i in range(n):
    Pi,Qi=input().split()
    if  int(Qi)- int(Pi) >1 :
        c+=1
print(c)
