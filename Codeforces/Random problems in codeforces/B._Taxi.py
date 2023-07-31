c=t=0
n= int(input())
groups=list(map(int,input().split()))
taxi=4
groups.sort() # 1 2 4 3 3

#print(groups)
if all(elem == 1 for elem in groups) and n >3:
 c=int(n/4)
else:
 for i in range(n):
    j=i+1
    
    while j <n:
        if groups[j]+groups[i]==4 and groups[j]!=0 and groups[i] !=0:
            #print(groups[i],groups[j],groups,sep="--")
            groups[i]=0
            groups[j]=0
            c+=1
            break
        j+=1
 if all(elem == 0 for elem in groups):
  t=0
 else:
  for i in range(0,n): #0 2 0 3 4
    t=0
    #print("group have =",groups[i])
    if taxi - groups[i] >= 0  and groups[i] !=0:
       taxi=taxi - groups[i]
       #print("taxi now have ",taxi)
    elif taxi - groups[i] < 0  and groups[i] !=0:
        c+=2
        #print("+1")
        taxi=4
        #print("\n new taxi ")
        t=1
    if taxi ==0:
        c+=1
        #print("+2")
        taxi=4
        #print("\n new taxi ")
        t=1
    if i == len(groups)-1 and taxi!=0 and t!=1 and taxi !=4:
        c+=1
        #print("last taxi have ",taxi)
        #print("+3")
#print(groups)
print(c)
