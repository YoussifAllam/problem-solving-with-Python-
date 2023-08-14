n=int(input())
l = list(map(int,input().split()))
def recursion(i,sum):
    if i==n:
        print(sum/n)
        return
    sum += l[i]
    recursion(i+1,sum)
recursion(0,0)
        