# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def transpose_matrix(matrix):
    """Transposes an M x N matrix (flips rows and columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty transposed matrix of size N x M
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
        
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Adds two matrices of the same dimensions element-wise."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(row)
        
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiplies an M x N matrix by an N x P matrix."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for r in range(rows_a):
        row = []
        for c in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[r][k] * matrix_b[k][c]
            row.append(dot_product)
        result.append(row)
        
    return result


def print_matrix(matrix):
    """Helper function to print a matrix cleanly."""
    for row in matrix:
        print(" ".join(str(val) for val in row))


def get_matrix_input(rows, cols, name="Matrix"):
    """Helper function to read matrix elements from the user."""
    print(f"Enter elements for {name} ({rows}x{cols}):")
    matrix = []
    for r in range(rows):
        row_input = input(f"Row {r + 1} ({cols} numbers separated by space): ").split()
        row = [float(val) if '.' in val else int(val) for val in row_input]
        matrix.append(row)
    return matrix


def main():
    try:
        print("=== PART A: Transpose Matrix ===")
        m = int(input("Enter number of rows (M): "))
        n = int(input("Enter number of columns (N): "))
        
        matrix_a = get_matrix_input(m, n, "Matrix A")
        
        print("\nOriginal Matrix:")
        print_matrix(matrix_a)
        
        print("\nTransposed Matrix:")
        print_matrix(transpose_matrix(matrix_a))
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()

