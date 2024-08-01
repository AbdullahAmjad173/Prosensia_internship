class MatrixDimensionError(Exception):
    pass

class MatrixTypeError(Exception):
    pass

def matrix_addition(matrix1, matrix2):
    # Check if both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise MatrixDimensionError("Matrices must have the same dimensions")
    
    # Perform matrix addition
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        new_row = []
        for elem1, elem2 in zip(row1, row2):
            if not isinstance(elem1, (int, float)) or not isinstance(elem2, (int, float)):
                raise MatrixTypeError("Matrices must contain only numbers")
            new_row.append(elem1 + elem2)
        result.append(new_row)
    
    return result

# calling function
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
try:
    result = matrix_addition(matrix1, matrix2)
    print(result)
except (MatrixDimensionError, MatrixTypeError) as e:
    print(e)
