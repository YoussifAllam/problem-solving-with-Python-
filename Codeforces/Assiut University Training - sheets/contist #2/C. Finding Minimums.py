def find_minimum_subarray(arr, k):
    min_value = float('inf')
    current_min = float('inf')
    
    for i, num in enumerate(arr):
        if num < current_min:
            current_min = num
        
        if i % k == k - 1 or i == len(arr) - 1:
            min_value = min(min_value, current_min)
            current_min = float('inf')
    
    return min_value


if __name__ == "__main__":
    N, K = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    
    result = [find_minimum_subarray(numbers[i:i+K], K) for i in range(0, N, K)]
    print(*result)
