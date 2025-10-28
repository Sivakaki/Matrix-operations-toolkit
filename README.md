# Matrix Operations Toolkit

A comprehensive Python library for performing various matrix operations using NumPy. This toolkit provides an interactive command-line interface for executing fundamental and advanced linear algebra operations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [License](#license)

## Features

- **Basic Operations**: Addition, subtraction, and element-wise multiplication
- **Advanced Operations**: Matrix multiplication, transpose, determinant, and inverse
- **Linear Algebra**: Trace, rank, eigenvalues, and eigenvectors
- **Interactive CLI**: User-friendly command-line interface for easy operation
- **Input Validation**: Comprehensive error handling and dimension checking
- **NumPy Integration**: Leverages NumPy for efficient computations

## Requirements

- Python 3.6 or higher
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/matrix-operations-toolkit.git
cd matrix-operations-toolkit
```

2. Install dependencies:
```bash
pip install numpy
```

## Usage

Run the toolkit with:
```bash
python matrix_operations_toolkit.py
```

The program will display an interactive menu with the following options:

```
1. Add Matrices
2. Subtract Matrices
3. Element-Wise Multiplication
4. Matrix Multiplication
5. Transpose of Matrix
6. Determinant of Matrix
7. Inverse of Matrix
8. Trace of Matrix
9. Eigenvalues and Eigenvectors
10. Rank of Matrix
0. Exit
```

Follow the on-screen prompts to input your matrices and select operations.

## Functions

### Basic Matrix Operations

**`add_matrices(arr1, arr2)`**
Adds two matrices element-wise. Requires matrices of identical dimensions.

**`sub_matrices(arr1, arr2)`**
Subtracts the second matrix from the first element-wise. Requires matrices of identical dimensions.

**`elemul_matrices(arr1, arr2)`**
Performs element-wise (Hadamard) multiplication. Requires matrices of identical dimensions.

### Matrix Transformations

**`matmul_matrices(arr1, arr2)`**
Performs standard matrix multiplication. Number of columns in arr1 must equal number of rows in arr2.

**`transpose_matrix(arr)`**
Returns the transpose of the input matrix.

### Matrix Properties

**`det_matrix(arr)`**
Calculates the determinant of a square matrix.

**`inv_matrix(arr)`**
Calculates the inverse of a square matrix. Raises an error if the matrix is singular.

**`trace_matrix(arr)`**
Calculates the trace (sum of diagonal elements) of a square matrix.

**`rank_of_matrix(arr)`**
Determines the rank of a matrix.

**`eigen_matrix(arr)`**
Computes eigenvalues and eigenvectors of a square matrix. Returns a tuple containing both.

### Utility Functions

**`input_matrix(name="matrix")`**
Prompts the user to input a matrix interactively. Validates row and column counts and returns a NumPy array.

## Examples

### Adding Two Matrices
```
Enter your choice: 1
Enter the number of rows in Matrix A: 2
Enter the number of columns in the Matrix A: 2
Enter the elements of Matrix A row by row (space-separated):
row1: 1 2
row2: 3 4
Enter the number of rows in Matrix B: 2
Enter the number of columns in the Matrix B: 2
Enter the elements of Matrix B row by row (space-separated):
row1: 5 6
row2: 7 8

Result (A + B): [[ 6  8]
                 [10 12]]
```

### Computing Eigenvalues and Eigenvectors
```
Enter your choice: 9
Enter the number of rows in matrix: 2
Enter the number of columns in the matrix: 2
Enter the elements of matrix row by row (space-separated):
row1: 1 0
row2: 0 2

Eigenvalues: [1. 2.]
Eigenvectors (columns): [[1. 0.]
                         [0. 1.]]
```

## Error Handling

The toolkit includes comprehensive error handling for common issues:

- **Dimension Mismatch**: Operations requiring equal dimensions validate input size
- **Singular Matrix**: Inverse operations check matrix determinant before computation
- **Non-Square Matrix**: Operations requiring square matrices validate shape
- **Invalid Input**: User input validation ensures correct data entry

All errors are caught and displayed with descriptive messages to guide the user.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

K Siva Rama Krishna

## Acknowledgments

- Built with [NumPy](https://numpy.org/)
- Inspired by linear algebra fundamentals
