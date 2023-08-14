n = int(input())
def print_rec(n):
    if n==1:
        print(n)
 
    if n>1:
        print(n,end=" ")
        print_rec(n-1)

print_rec(n)
