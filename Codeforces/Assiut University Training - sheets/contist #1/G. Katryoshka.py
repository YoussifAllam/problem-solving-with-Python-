eye, mouth, body = map(int, input().split())
res = 0
if eye == 0 or body == 0:
    print(0)
else:
    if (mouth >= eye and mouth >= body) or (mouth >= body and mouth < eye) or (mouth < body and mouth >= eye):
        res = min(eye, body)
        print(res)
    elif mouth < body and mouth < eye:
        res = mouth
        eye -= mouth
        body -= mouth
        res += min(eye // 2, body)
   
        print(res)