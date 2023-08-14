def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    quotient = n // 2
    remainder = n % 2
    return decimal_to_binary(quotient) + str(remainder)

def main():
    T = int(input().strip())

    for _ in range(T):
        N = int(input().strip())
        binary_representation = decimal_to_binary(N)
        print(binary_representation)

if __name__ == "__main__":
    main()
