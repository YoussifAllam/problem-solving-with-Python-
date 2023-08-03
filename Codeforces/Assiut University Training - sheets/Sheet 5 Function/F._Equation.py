def calculate_S(X, N):
    result = 0
    power = 0
    while power <= N:
        result += X**power
        power += 2
    result -= 1 # subtract X^(-1)
    return result

X, N = map(int, input().split())
S = calculate_S(X, N)
print(S)
