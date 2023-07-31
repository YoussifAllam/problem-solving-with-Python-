n=int(input()) #num of coins

list1=list(input().split()) # the coins' values

list1=[int(i) for i in list1] # convert values in list to int

b1=i=c=b2=0

list1=sorted(list1, reverse=True) # sort list in descending order

def suma(list2,j,n1):
    b2=0
    while j < n1 :
        b2+=list2[j]
        j+=1

    return b2

while i < n:
    b1+=int(list1[i])
    c+=1 # number of cois that the fist son will get it 
    b2=suma(list1,i+1,n) # Total coins values to be received by the next son
   
    if b1>b2:
        break

    i+=1

print(c)


