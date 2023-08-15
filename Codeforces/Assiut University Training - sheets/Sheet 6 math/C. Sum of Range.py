def sumOdd(num):
    res = (num + 1) // 2
    finalRes = res * res
    return finalRes

def sumEven(num):
    res = (num*(num+1))
    return res

num1,num2 = map(int,input().split())
start,end = (num2,num1) if num1 >= num2 else (num1,num2)

evenRes = sumEven(end//2) - sumEven((start-1) // 2)
oddRes = sumOdd(end) - sumOdd(start - 1)

print(evenRes+oddRes)
print(evenRes)
print(oddRes)