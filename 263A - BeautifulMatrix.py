'''
You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one.
Let's index the matrix rows by numbers from 1 to 5 from top to bottom,
let's index the matrix columns by numbers from 1 to 5 from left to right.
In one move, you are allowed to apply one of the two following transformations
to the matrix:

    Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
    Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5). 

You think that a matrix looks beautiful, if the single number one of
the matrix is located in its middle (in the cell that is on
the intersection of the third row and the third column).
Count the minimum number of moves needed to make the matrix beautiful.
================================
Input
The input consists of five lines, each line contains five integers:
the j-th integer in the i-th line of the input represents the element of
the matrix that is located on the intersection of the i-th row and
the j-th column. It is guaranteed that the matrix consists of 24 zeroes and
a single number one.
================================
Output
Print a single integer — the minimum number of moves needed to make
the matrix beautiful.
================================
Sample test(s)

Input
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
Output
3

Input
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
Output
1
'''
##              This is The FIRST solutuin
##                  Running Time   =======>>>   122 ms

## This method defines to return the '1' position in 2D list
##          return the row and column positions
def find_one_idx(matrx):
    row_idx = -1
    col_idx = -1
    for i in range(0, len(matrx)):
        for j in range(0, len(matrx[i])):
            if matrx[i][j] == '1':
                row_idx, col_idx = i, j
                break
        if row_idx != -1:
            break
    return row_idx, col_idx

## Intalize matrix 5*5 and get its data from user
matrix = [[0] * 5] * 5
for i in range(0, 5):
    matrix[i] = raw_input().split()

## ge one position
row_idx_counter, col_idx_counter = find_one_idx(matrix)
min_counter = 0

## loop until the indices equals to (2, 2) then break
##   with each increment add 1 to counter to print it as a minimum
##     moves value
while True:
    if row_idx_counter == 2 and col_idx_counter == 2:
        break
    if row_idx_counter > 2:
        row_idx_counter -= 1
        min_counter += 1
    elif row_idx_counter < 2:
        row_idx_counter += 1
        min_counter += 1
    if col_idx_counter > 2:
        col_idx_counter -= 1
        min_counter += 1
    elif col_idx_counter < 2:
        col_idx_counter += 1
        min_counter += 1


print(min_counter)

'''
##              This is The SECOND solutuin
##                  Running Time   =======>>>   124 ms

## Intalize matrix 5*5 and get its data from user
matrix = [[0] * 5] * 5
for i in range(0, 5):
    matrix[i] = raw_input().split()
    if '1' in matrix[i]:
          row_idx_counter, col_idx_counter = i, matrix[i].index('1')


min_counter = 0

## loop until the indices equals to (2, 2) then break
##   with each increment add 1 to counter to print it as a minimum
##     moves value
while True:
    if row_idx_counter == 2 and col_idx_counter == 2:
        break
    if row_idx_counter > 2:
        row_idx_counter -= 1
        min_counter += 1
    elif row_idx_counter < 2:
        row_idx_counter += 1
        min_counter += 1
    if col_idx_counter > 2:
        col_idx_counter -= 1
        min_counter += 1
    elif col_idx_counter < 2:
        col_idx_counter += 1
        min_counter += 1


print(min_counter)

'''
