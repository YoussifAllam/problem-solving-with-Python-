s1=input()
t=0

if int (s1)%4 == 0 or int (s1)%7 == 0 or int (s1)%4==0 or int (s1)%7==0 or int (s1)%44==0 or int (s1)%47==0 or int (s1)%74==0 or int (s1)%77==0 or int (s1)%444==0 or int (s1)%447==0 or int (s1)%474==0 or int (s1)%744==0 or int (s1)%477==0 or int (s1)%747==0 or int (s1)%774==0 or int (s1)%777==0 :
     print("YES") 
else:
 for i in range(len(s1)):
    
    if int(s1[i])==4  or int(s1[i])==7 :
        t=1
    else:
        t=0
        break


 if t==1:
    print("YES")
 else:
    print("NO")