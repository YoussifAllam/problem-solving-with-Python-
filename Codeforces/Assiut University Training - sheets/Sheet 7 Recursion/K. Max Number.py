def find_max(arr, n):
    if n == 1:
        return arr[0]
    max_in_rest = find_max(arr, n - 1)
    return max(max_in_rest, arr[n - 1])

if __name__ == "__main__":
    N = int(input())
    array = list(map(int, input().split()))
    print(find_max(array, N))
