s = input()  
target = "hello" 
j = 0  
for char in s:
    if j == len(target):  
        break
    if char == target[j]:  
        j += 1  
if j == len(target):  
    print("YES")
else:
    print("NO")
