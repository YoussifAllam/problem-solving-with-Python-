def get_avg(list1):
    print(sum(list1)/len(list1))
    
    
n=int(input())
list1=list(map(float,input().split()))
get_avg(list1)