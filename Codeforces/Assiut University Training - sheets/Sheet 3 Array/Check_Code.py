a, b = map(int, input().split())
s = input()

if len(s) != a + b + 1:
    print("No")
elif s[a] != '-':
    print("No")
else:
    for i in range(a + b + 1):
        if i == a:
            continue
        if not s[i].isdigit():
            print("No")
            break
    else:
        print("Yes")
s