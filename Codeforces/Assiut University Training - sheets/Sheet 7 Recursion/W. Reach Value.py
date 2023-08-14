input1 = 0
def reachValue(num): # 1
    global input1
    if input1 < num:
        return False
    elif input1 == num:
        return True
    else:
        return reachValue(num * 10) or reachValue(num * 20)

tests = int(input()) 
while tests > 0: 
    input1 = int(input())
    if reachValue(1):
        print("YES")
    else:
        print("NO")
    tests -= 1