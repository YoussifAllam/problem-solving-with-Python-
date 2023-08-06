n = int(input())

for i in range(n):
    s, t = input().split()
    new_string = ""
    min_len = min(len(s), len(t))
    for j in range(min_len):
        new_string += s[j] + t[j]
    if len(s) > len(t):
        new_string += s[min_len:]
    else:
        new_string += t[min_len:]
    print(new_string)
