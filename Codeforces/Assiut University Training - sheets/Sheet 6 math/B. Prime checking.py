def is_prime(num):
    is_prime = 'YES'

    if num == 0 or num == 1:
        is_prime = 'NO'

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = 'NO'
            break

    return is_prime

from math import sqrt
n = int(input())
print(is_prime(n))




