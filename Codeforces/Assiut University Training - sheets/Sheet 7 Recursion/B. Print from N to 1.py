n = int(input())

def print_rec(i):
    if n>=i:
        print(i)
        print_rec(i+1)

print_rec(1)
