'''
DZY loves chessboard, and he enjoys playing with it.

He has a chessboard of n rows and m columns.
Some cells of the chessboard are bad, others are good.
For every good cell, DZY wants to put a chessman on it.
Each chessman is either white or black.
After putting all chessmen, DZY wants that no two chessmen with
the same color are on two adjacent cells.
Two cells are adjacent if and only if they share a common edge.

You task is to find any suitable placement of chessmen on the given chessboard.
========================================
Input
The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 100).

Each of the next n lines contains a string of m characters:
the j-th character of the i-th string is either "." or "-".
A "." means that the corresponding cell (in the i-th row and the j-th column)
is good, while a "-" means it is bad.
========================================
Output
Output must contain n lines, each line must contain a string of m characters.
The j-th character of the i-th string should be either "W", "B" or "-".
Character "W" means the chessman on the cell is white,
"B" means it is black, "-" means the cell is a bad cell.

If multiple answers exist, print any of them.
It is guaranteed that at least one answer exists.
========================================
Sample test(s)

Input
1 1
.
Output
B

Input
2 2
..
..
Output
BW
WB

Input
3 3
.-.
---
--.
Output
B-B
---
--B
'''

##              Running Time ===>>> 77 ms

data = input().split()

N, M = int(data[0]), int(data[1])

chess = [None] * N
for i in range(N):
    chess[i] = input()

'''
    ##  check if this index contian '.' char so will replace ti with B or W
    ##      if the sum of (i+j) is even so replace it with W
    ##      Otherwise, replace it with B
    ##  if contains '-' let it as its
'''
answer = [None] * N
for i in range(N):
    new = [None] * M
    for j in range(M):
        if chess[i][j] == '.':
            if (i+j)%2 == 0:
                new[j] = 'W'
            else:
                new[j] = 'B'
        elif chess[i][j] == '-':
            new[j] = '-'

    answer[i] = "".join(new)

print("\n".join(map(str, answer)))


