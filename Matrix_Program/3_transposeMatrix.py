# Define a matrix A  
A = [[5, 4, 3],  
     [2, 4, 6],  
     [4, 7, 9],  
     [8, 1, 3]]  

# Define an empty matrix for the transpose result
# The transpose of A will be a 3x4 matrix
transResult = [[0, 0, 0, 0],    
               [0, 0, 0, 0],  
               [0, 0, 0, 0]]  

# Use nested for loop to compute the transpose of matrix A  
for a in range(len(A)):         # Iterate over rows of A
    for b in range(len(A[0])):  # Iterate over columns of A
        transResult[b][a] = A[a][b]  # Store the transpose result in the empty matrix          

# Printing result
print("The transpose of matrix A is: ")  
for res in transResult:    
    print(res)  
