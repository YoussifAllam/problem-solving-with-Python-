n=int(input())
list1=list(input().split())
list1=[int(i) for i in list1] 
nagtivel=[]
even=[]
odd=[]
Positive=[]


for i in range(0,n):
    if list1[i] <0:
        nagtivel+="a"

    if list1[i] >0:
         Positive+="a"

    if list1[i] %2==0:
        even+="a" 

    else:
        odd+="a"

print("Even: ",len(even))
print("Odd: ",len(odd))
print("Positive: ",len(Positive))
print("Negative: ",len(nagtivel))
    