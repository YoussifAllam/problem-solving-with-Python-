a ,b,q= map(int,input().split())

res = q % 3
if res == 1:
    print(a)
elif res == 2:
    print(b)
else:
    print(a ^ b)