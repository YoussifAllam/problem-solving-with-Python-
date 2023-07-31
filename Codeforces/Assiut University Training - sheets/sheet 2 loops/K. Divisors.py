n=int(input())
i=1

def check(number :int):
    if n %number==0:
        print(number)


while i <= n:
    check(i)
    i+=1
