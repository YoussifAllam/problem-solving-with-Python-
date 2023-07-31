n=input()
i=len(n)-1
newn=""
while i > -1:
    if len(newn)==0: # to make first number not = zero
        if int(n[i]) == 0:
            i-=1
        else:
          newn+=n[i]
          i-=1
    else:
     newn+=n[i]
     i-=1

print(newn)
if n== newn:
    print("YES")
else:
    print("NO")