import math
n=int(input())
t=0

div = math.ceil(n/2)+1
for i in range(2,div):
    res=n /i
    if  res.is_integer()== True: # not prime
        t=1
        break
   
if t==1:
  print("NO")
elif t==0 and n>1:
  print("YES")
