import math
num1 , num2= map(int,input().split())
 
print(math.comb(num1, num2), end=" ") # n choose k
print(math.factorial(num1) // math.factorial(num1 - num2)) # n permute k