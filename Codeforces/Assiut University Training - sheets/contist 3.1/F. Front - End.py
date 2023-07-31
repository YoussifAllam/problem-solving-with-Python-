n = int(input())
l = list(map (int,input().split()))
a = []
while l :
    a.append(l.pop(0))
    try :
       a.append(l.pop(-1))
    except:
        continue
print(*a)
