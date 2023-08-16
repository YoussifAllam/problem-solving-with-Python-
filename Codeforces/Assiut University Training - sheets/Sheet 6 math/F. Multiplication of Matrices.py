# Read the input
r1, c1 = map(int, input().split()) # 2 2
# Initialize the first matrix
arr1 = []
# Loop over the rows
for i in range(r1): # i = 1 i<2
    # Read the row and append it to the matrix
    row = list(map(int, input().split())) # i = 0  z=0  z=1    i = 1  z= 0  z = 1
    arr1.append(row)

# Read the input
r2, c2 = map(int, input().split()) # 2 2
# Initialize the second matrix
arr2 = []
# Loop over the rows
for i in range(r2): # i = 1 i<2
    # Read the row and append it to the matrix
    row = list(map(int, input().split())) # i = 0  z=0  z=1    i = 1  z= 0  z = 1
    arr2.append(row)

# Initialize the result matrix with zeros
result = [[0 for j in range(c2)] for i in range(r1)]

# Loop over the rows of the first matrix
for i in range(r1): # i=0                                 i<2
    # Loop over the columns of the second matrix
    for j in range(c2): # j=1                               j<3
        # Loop over the columns of the first matrix or rows of the second matrix
        for k in range(c1): # k=0                            k<3
            # Update the result matrix with the product of the corresponding elements
            result[i][j] += arr1[i][k] * arr2[k][j]
            # result[0][1] = arr1[0][0] * arr2[0][1];
            # result[0][1] = arr1[0][1] * arr2[1][1];
            # result[0][1] = arr1[0][2] * arr2[2][1];

# Loop over the rows of the result matrix
for i in range(r1): # i = 1 i<2
    # Loop over the columns of the result matrix
    for j in range(c2): # j < 2 
        # Print the element with a space after it
        print(result[i][j], end=" ") # i = 0  j=0  j=1    i = 1  j= 0  j = 1
    # Print a new line after each row
    print()