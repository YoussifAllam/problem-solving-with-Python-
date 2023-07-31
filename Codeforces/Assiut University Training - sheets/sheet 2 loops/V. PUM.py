t=int(input())
line=c2=0
i=1
while True:
 if line!=t:
    print(i,end=" ")
    c2+=1
    if c2 %3==0:
        print("PUM")
        i+=2
        line+=1
        continue
 
 else:
     break
 i+=1
