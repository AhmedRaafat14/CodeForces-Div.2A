'''
Simon has a rectangular table consisting of n rows and m columns.
Simon numbered the rows of the table from top to bottom starting
from one and the columns — from left to right starting from one.
We'll represent the cell on the x-th row and the y-th column as a
pair of numbers (x, y). The table corners are cells:
(1, 1), (n, 1), (1, m), (n, m).

Simon thinks that some cells in this table are good.
Besides, it's known that no good cell is the corner of the table.

Initially, all cells of the table are colorless.
Simon wants to color all cells of his table.
In one move, he can choose any good cell of table (x1, y1),
an arbitrary corner of the table (x2, y2) and color all cells of the table
(p, q), which meet both inequations: min(x1, x2) ≤ p ≤ max(x1, x2),
min(y1, y2) ≤ q ≤ max(y1, y2).

Help Simon! Find the minimum number of operations needed to color all
cells of the table. Note that you can color one cell multiple times.
====================================
Input
The first line contains exactly two integers n, m (3 ≤ n, m ≤ 50).

Next n lines contain the description of the table cells.
Specifically, the i-th line contains m
space-separated integers ai1, ai2, ..., aim.
If aij equals zero, then cell (i, j) isn't good.
Otherwise aij equals one. It is guaranteed that at least one cell is good.
It is guaranteed that no good cell is a corner.
====================================
Output
Print a single number — the minimum
number of operations Simon needs to carry out his idea.
====================================
Sample test(s)

Input
3 3
0 0 0
0 1 0
0 0 0
Output
4

Input
4 3
0 0 0
0 0 1
1 0 0
0 0 0
Output
2
'''

##                  Running Time   ===>>>   62 ms

data = input().split()

N, M = int(data[0]), int(data[1])

table = []
for i in range(N):
    table.append(input().split())

answer = 0

##   If there's 1 in first or last row or first and last column so answer
##      will be :      2
##  Otherwise, will equal to 4

## for first row
if any(e == '1' for e in table[0]):
    answer = 2
##  for last row
elif any(e == '1' for e in table[-1]):
    answer = 2
## for first and  last column
else:
    for i in range(N):
        if table[i][0] == '1':
            answer = 2
        elif table[i][-1] == '1':
            answer = 2

if answer == 0:
    print('4')
else:
    print(answer)
        
