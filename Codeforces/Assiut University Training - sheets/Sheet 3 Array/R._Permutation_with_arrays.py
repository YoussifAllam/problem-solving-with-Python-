n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c=0
for i in range(n):
  l=a[i]
  s1=a.count(l)
  s2=b.count(l)
  if s1==s2:
      c+=1
if c==n:
    print("yes")
else:
    print("no")


#anthor solution
""" 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))



a.sort()
b.sort()
  if a == b:
    print("yes")
  else:
    print("no")

"""