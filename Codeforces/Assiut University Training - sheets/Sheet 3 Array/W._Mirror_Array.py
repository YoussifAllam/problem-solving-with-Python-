n,m=map(int,input().split())
for i in range(n):
    list1=list(map(int,input().split()))
    list2=[]
    i=m-1
    while i >-1:
        list2.append(list1[i])
        i-=1
    for j in range(m):
        print(list2[j],end=" ")
    print()

    #anthor solution
    '''
    list1=sorted(list1, reverse=True)
    for j in range(m):
        print(list2[j],end=" ")
    print()

    '''