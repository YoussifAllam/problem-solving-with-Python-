from  math import sqrt

num = int(input()) # 18

flag = 0

for i in range(2, int(sqrt(num)) + 1): # i = 3
    
    counter = 0
    
    while num % i == 0: 
        counter += 1 
        num //= i 
    
    if counter > 0 and flag > 0:
        print("*", end="")
    
    if counter > 0:
        print(f"({i}^{counter})", end="")
        flag = 1
    
    if num == 1:
        break

if num > 1 and flag:
    print("*", end="")

if num > 1:
    print(f"({num}^{1})", end="")