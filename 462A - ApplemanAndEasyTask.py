'''
Toastman came up with a very easy task. He gives it to Appleman,
but Appleman doesn't know how to solve it. Can you help him?

Given a n × n checkerboard. Each cell of the board has either character 'x',
or character 'o'. Is it true that each cell of the board has even number
of adjacent cells with 'o'?
Two cells of the board are adjacent if they share a side.
===================================
Input
The first line contains an integer n (1 ≤ n ≤ 100).
Then n lines follow containing the description of the checkerboard.
Each of them contains n characters (either 'x' or 'o') without spaces.
===================================
Output
Print "YES" or "NO" (without the quotes) depending on the answer to
the problem.
===================================
Sample test(s)

Input
3
xxo
xox
oxx
Output
YES

Input
4
xxxo
xoxo
oxox
xxxx
Output
NO
'''

##          Running Time ====>>>>  61 ms

N = int(input())

board = [None] * N
for i in range(N):
    board[i] = input()

is_even = 0
'''
    for each cell it have 4 adjacent:
         (i-1, j), (i+1, j), (i, j-1), (i, j+1)
    for example: (1, 1)
         (0, 1), (2, 1), (1, 0), (1, 2)
    so check on them if any of them equal to 'o' and  count it
    then check if this counter odd so you should break and answer by NO
    if it even go on till the end if it still even print 'YES'
'''
for i in range(N):
    if is_even == 1:
        break
    for j in range(N):
        count_adjacent_cells = 0
        if i > 0 and board[i - 1][j] == 'o':
            count_adjacent_cells += 1
        if i < N - 1 and board[i + 1][j] == 'o':
            count_adjacent_cells += 1
        if j > 0 and board[i][j - 1] == 'o':
            count_adjacent_cells += 1
        if j < N - 1 and board[i][j + 1] == 'o':
            count_adjacent_cells += 1

        if count_adjacent_cells%2 != 0:
            is_even = 1
            break

if is_even == 0:
    print('YES')
else:
    print('NO')
        
        
