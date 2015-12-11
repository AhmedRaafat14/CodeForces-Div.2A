'''
You are given a rectangular cake, represented as an r × c grid.
Each cell either has an evil strawberry, or is empty.
For example, a 3 × 4 cake may look as follows:

            S...
            ....
            ..S.

The cakeminator is going to eat the cake! Each time he eats,
he chooses a row or a column that does not contain any evil
strawberries and contains at least one cake cell that has not been eaten before,
and eats all the cake cells there. He may decide to eat any number of times.

Please output the maximum number of cake cells that the cakeminator can eat.
=======================================
Input
The first line contains two integers r and c (2 ≤ r, c ≤ 10),
denoting the number of rows and the number of columns of the cake.
The next r lines each contains c characters — the j-th character of
the i-th line denotes the content of the cell at row i and column j,
and is either one of these:

    - '.' character denotes a cake cell with no evil strawberry;
    - 'S' character denotes a cake cell with an evil strawberry. 
=======================================
Output
Output the maximum number of cake cells that the cakeminator can eat.
=======================================
Sample test(s)

Input
3 4
S...
....
..S.
Output
8
'''

##          Running Time ===>>> 124 ms

data = input().split()

R, C = int(data[0]), int(data[1])

cake = [[None] * C] * R

for i in range(R):
    cake[i] = input()

eaten_cake = 0

## For rows
for i in range(R):
    if cake[i].count('S') == 0:
        eaten_cake += C
        cake[i] = '1' * C
        continue

## For Columns
for j in range(C):
    S_flag = 0
    for i in range(R):
        if cake[i][j] == 'S':
            S_flag = 1
            break
    if S_flag == 1:
        continue
    else:
        for i in range(R):
            if cake[i][j] == '.':
                eaten_cake += 1

print(eaten_cake)
