n , x, y = map(int, input().split())
matrix = []
for i in range(n):
    row  = list(map(int, input().split()))
    matrix.append(row)  
#  print(matrix)

# Swap Row
matrix[x-1] , matrix[y-1] = matrix[y-1] , matrix[x-1]

for i in range (n):
    matrix[i][x-1] , matrix[i][y-1] = matrix[i][y-1]  , matrix[i][x-1] 


for i in matrix:
   print(*i)

'''
4 3 1

4 3 1
1 2 3 -5
-5 4 0 3
7 7 1 2
40 6 5 11


[[ 1, 2, 3, -5 ], 
 [-5, 4, 0,  3 ],
 [ 7, 7, 1,  2  ], 
 [40, 6, 5, 11]
 
 ]


'''