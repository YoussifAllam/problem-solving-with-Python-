n = input()
if '=' in n:
    idx = n.find('=')
    n=n[:idx]+'='+n[idx:]
    #print(n)
if eval(n):
    print("Yes")
else:
    n=n[:idx]
    print(eval(n))