seet = int(input())
row = seet // 4 

if row % 2 == 0: 
    column = seet % 4 
else: 
    column = 3 - (seet % 4) 
print(row, column)