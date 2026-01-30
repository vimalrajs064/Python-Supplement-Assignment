# Problem 71: Transpose a matrix
# Find and fix the error
def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

mat = [[1, 2, 3], [4, 5, 6]]
print(f"Transposed: {transpose(mat)}")