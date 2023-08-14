n = int(input())
fac = 1
def recursion ( n  ) :
  global fac
  if n >0:
    fac*=n
    recursion(n-1)
  

recursion(n)
print(fac)