n=int(input())
primary_diagonal=[]
secondary_diagonal=[]
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            primary_diagonal.append(a[i][j])
k=0
h=n-1
while k<n:
     secondary_diagonal.append(a[k][h])
     k+=1
     h-=1

print(abs(sum(primary_diagonal)-sum(secondary_diagonal)))

