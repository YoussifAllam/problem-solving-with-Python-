t=int(input())
l=0
test=[]
for i in range(t):
   l=0
   n=int(input())
   s=input()
   if len(s)==1:
      print("YES")
      
   else:
       
    for g in s:
        if g not in test:
            test.append(g)
            if len(test) >3:
                print("NO")
                break
    if  len(test) == 3:
 
     for h in range(len(s)):
     
      if h !=len(s)-1:
        if s[h]==s[h+1]:
            print("NO")
            #print(s[i],s[i+1])
            l=1
            break
      else:
            if s[h]==s[h-1]:
                print("NO")
                #print(s[i],s[i-1])
                l=1
                break
     if l!=1:
       print("YES")
 



