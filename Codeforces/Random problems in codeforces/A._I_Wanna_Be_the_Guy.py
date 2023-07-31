n=int(input())
little_x=list(map(int,input().split()))
#print("bbbb")
little_y=list(map(int,input().split()))
little_x = little_x[1:] + little_y[1:]
little_x.sort()
unique_numbers = set(little_x)
#print("unique_numbers = ",unique_numbers,"\n")
total = int(n * (n + 1) / 2)
#print("total=",total)

Sum = sum(unique_numbers)
#print("sum=",Sum)
#print("==",little_x[len(little_x)-1])
if total == Sum:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

