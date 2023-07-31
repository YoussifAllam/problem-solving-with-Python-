import math 
a,b=map(int,input().split())
print(f"floor {a} / {b} = {a // b}")
print(f"ceil {a} / {b} = {math.ceil(a / b)}")
if a / b  -  0.5 == a//b:
    print(f"round {a} / {b} = {round(a / b + 0.5)}")
else: print(f"round {a} / {b} = {round(a / b )}")