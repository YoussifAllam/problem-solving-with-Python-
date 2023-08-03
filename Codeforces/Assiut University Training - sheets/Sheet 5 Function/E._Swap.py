
def f_swap(a,b):
    temp = a
    a=b
    b=temp
    print(a,b)

a , b = map( int , input().split() )
f_swap(a,b)




