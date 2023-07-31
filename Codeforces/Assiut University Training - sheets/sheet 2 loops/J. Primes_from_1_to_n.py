n = int(input())

# Initialize a list to store prime numbers
primes = []

# Iterate over the range [2, N] and check if each number is prime
for num in range(2, n+1):
     
    
    # If the number is prime, add it to the list of prime numbers
    if is_prime:
        primes.append(num)

# Print the list of prime numbers separated by a space
print(' '.join(str(num) for num in primes))
