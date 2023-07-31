import math

numberTest = int(input())

for i in range(numberTest):
    num = int(input())
    ones = 0
    while num > 0:
        if num % 2 == 1:
            ones += 1
        num //= 2
    sum = 0
    for z in range(ones):
        sum += 1 * math.pow(2, z)   
    print(int(sum))