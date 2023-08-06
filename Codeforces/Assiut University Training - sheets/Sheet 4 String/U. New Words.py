value = input() # "abc"    ['a','b','c']
size = len(value)
e = 0
g = 0
y = 0
p = 0
t = 0
for i in range(size):
    if value[i] == 'e' or value[i] == 'E':
        e += 1
    elif value[i] == 'g' or value[i] == 'G':
        g += 1
    elif value[i] == 'y' or value[i] == 'Y':
        y += 1
    elif value[i] == 'p' or value[i] == 'P':
        p += 1
    elif value[i] == 't' or value[i] == 'T':
        t += 1

# 5 6 7 8 9
#   5   7   9
#     5    9
#        5
min1 = min(e, g) # e g  ==> min1 
min2 = min(y, p) # y p  ==> min2
min3 = min(min1, min2)
print(min(min3, t))