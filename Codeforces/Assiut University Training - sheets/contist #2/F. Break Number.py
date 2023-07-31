def max_divisions_by_two(numbers):
    max_divisions = 0
    
    for x in numbers:
        divisions = 0
        while x % 2 == 0:
            x //= 2
            divisions += 1
        max_divisions = max(max_divisions, divisions)
    
    return max_divisions

if __name__ == "__main__":
    N = int(input())
    
    numbers = list(map(int, input().split()))
    
    result = max_divisions_by_two(numbers)
    print(result)
