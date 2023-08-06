value = input()
sub1 = ""
sub2 = ""
myValue = value 

smallString = value
for i in range(len(value) - 1):
    sub1 += value[i]
    myValue = myValue[1:] 
    sub2 = myValue 
    sub1 = ''.join(sorted(sub1)) 
    sub2 = ''.join(sorted(sub2)) 
    smallString = min(smallString, sub1 + sub2)
print(smallString)