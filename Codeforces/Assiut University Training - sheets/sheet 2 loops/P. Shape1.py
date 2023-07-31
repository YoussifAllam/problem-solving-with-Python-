n=int(input())
for i in range (n):
    s=input()
    j=len(s)-1
    while j>-1:
        print(s[j],end=" ")
        j-=1
    print()