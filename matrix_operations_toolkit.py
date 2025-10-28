import numpy as np

def add_matrices(arr1,arr2):
    """Add two matrices element-wise."""
    if arr1.shape != arr2.shape:
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return arr1+ arr2



def sub_matrices(arr1,arr2):
    """Subtract two matrices element-wise."""
    if arr1.shape != arr2.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    return arr1-arr2



def elemul_matrices(arr1,arr2):
    """Multiply two matrices element-wise(Hadamard Product)"""
    if arr1.shape != arr2.shape:
        raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
    
    return arr1*arr2



def matmul_matrices(arr1,arr2):
    """Perform Matrix Multiplication."""
    if arr1.shape[1] != arr2.shape[0]:
        raise ValueError ("number of columns of arr1 must equal to number of rows of arr2")
    
    return np.dot(arr1,arr2)



def transpose_matrix(arr):
    """Return the transpose of matrix."""
    
    return  arr.T



def det_matrix(arr):
    """Calculate the determinant of a square matrix."""
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Matrix must be square to calculate determinant.")
    
    return np.linalg.det(arr)



def inv_matrix(arr):
    """Calculate the inverse of a square matrix."""    
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Matrix must be square to calculate inverse.")

    det = np.linalg.det(arr)
    if np.isclose(det,0):
        raise ValueError("Singular Matrix, Inverse not Possible")
    
    return np.linalg.inv(arr)



def trace_matrix(arr):
    """Calculate the trace(sum of diagonal elements) of a square matrix."""
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("Matrix must be square to calculate trace.")

    return np.trace(arr)



def rank_of_matrix(arr):
    """Calculate the rank of a matrix"""
    
    return np.linalg.matrix_rank(arr)



def eigen_matrix(arr):
    """calculate eigenvalues and eigenvectors of a square matrix"""
    if arr.shape[0] != arr.shape[1]:
        raise ValueError ("Matrix must be square to calculate eigenvalues/eigenvectors.")
    
    values,vectors = np.linalg.eig(arr)

    return values,vectors



def input_matrix(name ="matrix"):
    """Prompt user to input a matrix."""
    rows = int(input(f"Enter the number of rows in {name} : "))
    cols = int(input(f"Enter the number of columns in the {name} : "))
    print(f"Enter the elements of {name} row by row (space-seperated) : ")

    matrix = []

    for i in range (rows):
        row = list(map(float,input(f"row{i+1} : ").split()))

        if len(row) != cols:
            print(f"Error : Excepted {cols} values.")
            return input_matrix(name)
        matrix.append(row)

    return np.array(matrix)



def main ():
    """Main function to run the MATRIX OPERATION TOOLKIT"""
    # set Numpy print options for cleaner input
    np.set_printoptions(precision=4, suppress=True)


    print("======WELCOME TO MATRIX OPERATIONS TOOLKIT======")


    while True:
        print("\n======MENU======")
        print("1.Add Matrices")
        print("2.Subtract Matrices")
        print("3.Element-Wise Multiplication")
        print("4.Matrix Multiplication")
        print("5.Transpose of  Matrix")
        print("6.Determinant of matrix")
        print("7.Inverse of Matrix")
        print("8.Trace of Matrix")
        print("9.Eigenvalues and Eigenvectors")
        print("10.Rank of Matrix")
        print("0.Exit")


        choice = input("Enter your choice : ").strip()

        try:
            if choice == "1":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = add_matrices(A,B)
                print("\nResult(A + B) :",result)


            elif choice == "2":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = sub_matrices(A,B)
                print("\nResults(A - B):",result)


            elif choice == "3":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = elemul_matrices(A,B)
                print("\nResults(A ⊙ B):",result)


            elif choice == "4":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")
                result = matmul_matrices(A,B)
                print("Results : \n",matmul_matrices(A,B))


            elif choice == "5":
                A = input_matrix()
                result = transpose_matrix(A)
                print("\nTranspose:",result)


            elif choice == "6":
                A = input_matrix()
                result = det_matrix(A)
                print(f"\nDeterminant: {result:.4f}")


            elif choice == "7":
                A = input_matrix()
                result = inv_matrix(A)
                print("\nInverse:",result)


            elif choice == "8":
                A = input_matrix()
                result = trace_matrix(A)
                print(f"\nTrace: {result:.4f}")


            elif choice == "9":
                A = input_matrix()
                values,vectors = eigen_matrix(A)
                print("\nEigenvalues :",values)
                print("\nEigenvectors(columns) : ",vectors)


            elif choice == "10":
                A = input_matrix()
                result = rank_of_matrix(A)
                print("\nRank: ",result)


            elif choice == "0":
                print("Thank you for using Matrix Operations Toolkit!")
                print("Goodbye!")
                break


            else:
                print("Invalid choice! Please enter a number from the menu.")
        

        except ValueError as ve:
            print(f"\nError : {ve}")
        except Exception as e:
            print(f"\nUnexpected error : {e}")


if __name__ == "__main__":
    main()