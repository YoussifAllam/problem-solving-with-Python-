n = int (input())
c = 1
def recursion(n):
    global c
    if n == 1:
        return 
    
    if n %2 == 0:
        c+=1
        recursion(n/2)
    else:
        c+=1
        recursion(3*n+1)
    

recursion(n)
print(c)

# 3,10,5,16,8,4,2,1
 