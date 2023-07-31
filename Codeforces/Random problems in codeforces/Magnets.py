n=int(input())
c=i=k=p=0
list1=[]
for j in range(n):
    item =input()
    list1.append(item)
#print("c1=",c)

def loop1(list2,n1):
   global c
   global k
   while k < n1:
      if k != n1-1:
          if list2[k]==list2[k+1]:
             p=0
          else:
             break
      else:
          if list2[k]==list2[k-1]:
              p=0
          else:
                  c+=1
       
      k+=1
   c+=1
   print("c1",c)
   return 0



loop1(list1,n)
   
print(">>>>",c)

