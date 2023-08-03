import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# main function to handle input/output
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if is_prime(n):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
