list1=[]
def printa(n):
    global list1
    for i in range(1,n+1):
        list1.append(str(i))
n1=int(input())
printa(n1)
print(" ".join(list1))