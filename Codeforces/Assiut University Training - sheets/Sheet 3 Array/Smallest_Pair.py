list_sum=[]
t=int(input())
for a in range(t):
        list_sum=[]
        t2=int(input())
        list1=list(input().split())
        list1=[int(i) for i in list1]
        i=1
        while i<t2:
            j=i+1
            while j<=t2:
                list_sum.append(list1[i-1]+list1[j-1]+int(j)-int(i))
                j+=1
            i+=1
        print(min(list_sum) )
