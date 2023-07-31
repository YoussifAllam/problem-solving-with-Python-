s1=input()
s2=input()
s3=""
i=0
for digit in s1:
    if digit == s2[i]:
        s3+=str(0)
    else:
        s3+=str(1)
    i+=1
print(s3)
