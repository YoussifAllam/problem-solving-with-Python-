
def if_odd(n1):
    if n % 2 !=0:
        #print("done 1")
        return True

def check(n1):
    binary= bin(n)[2:]
    return binary == binary[::-1]

n=int(input())
rus1= check(n)
rus2=if_odd(n) 
if rus1 == True and rus2 == True:
    print("YES")
else:
    print("NO")
