# Matrix multiplication using nested for loops

# Initialize the value of A and B matrix    
A = [[5, 4, 3],    
     [2, 4, 6],    
     [4, 7, 9]]      

B = [[3, 2, 4],    
     [4, 3, 6],    
     [2, 7, 5]]     

# Define an empty matrix to store multiplication result    
multiResult = [[0, 0, 0],      
               [0, 0, 0],      
               [0, 0, 0]]    

# Using nested for loops for matrix multiplication    
for m in range(len(A)):       # Iterate through rows of A
    for n in range(len(B[0])):  # Iterate through columns of B
        for o in range(len(B)):  # Iterate through rows of B (which is the same as columns of A)
            multiResult[m][n] += A[m][o] * B[o][n]  # Store multiplication result in the result matrix    

# Printing multiplication result
print("The multiplication result of matrix A and B is: ")    
for res in multiResult:      
    print(res)   
