n=int(input())
list1=list(input().split())
t=i=0
while i < n:
    if int(list1[i]) == 1 :
        t=1
        print("HARD")
        break
    i+=1


if t  == 0:
    print("EASY")
