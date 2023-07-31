n=int(input())
Fibonacci=[0,1]

for i in range(2,n):
   Fibonacci.append(Fibonacci[i-1]+Fibonacci[i-2])

print(Fibonacci[n-1])

