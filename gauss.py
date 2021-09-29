import numpy as np

# Data import into matrix-form

file = open("matrix.csv")
A = np.loadtxt(file, delimiter=",")

print(A)

num_rows, num_cols = A.shape

# if first element of the first row is zero exchange the rows (I put it to the bottom of the matrix)
for j in range(0, num_rows-1):
    if A[j][j] == 0:
        sor = A[j]
        A = np.delete(A, j, 0)
        A = np.append(A, [sor], 0)

# eliminate the first elements of the rows
    for i in range(1, num_rows-j):
        if A[j + i][j] != 0:
            A[j + i] = A[j + i] - A[j] * (A[j + i][j]/A[j][j])

    print(A)
    print(A.round(2))
