t = int(input())

for i in range(t):
 n = input()
 i = 0
 l= len(n)
 def print_rec(i,n,l):
    if i == l-1:
       print(n[i])
    if i<l-1:
        print(n[i],end=" ")
        print_rec(i+1,n,l)

 print_rec(0,n,l)
