n = int(input())
def print_rec(n):
    if n>0:
        print('I love Recursion')
        print_rec(n-1)

print_rec(n)
