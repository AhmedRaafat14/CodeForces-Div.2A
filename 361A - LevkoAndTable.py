'''
Levko loves tables that consist of n rows and n columns very much.
He especially loves beautiful tables. A table is beautiful to Levko
if the sum of elements in each row and column of the table equals k.

Unfortunately, he doesn't know any such table. Your task is to help
him to find at least one of them.
=======================================
Input
The single line contains two integers, n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 1000).
=======================================
Output
Print any beautiful table. Levko doesn't like too big numbers,
so all elements of the table mustn't exceed 1000 in their absolute value.

If there are multiple suitable tables, you are allowed to print any of them.
=======================================
Sample test(s)

Input
2 4
Output
1 3
3 1

Input
4 7
Output
2 1 0 4
4 0 2 1
1 3 3 0
0 3 2 2
'''

##          Running Time  ===>>>  93 ms

data = input().split()

N, K = int(data[0]), int(data[1])

table = []

##  one of solutions all diganol elements equals to K this make
##  sum of each row and column is equal
col = 0
while col < N:
    tmp = [0] * N
    tmp[col] = K
    table.append(tmp)
    col += 1

for row in table:
    print(" ".join(map(str, row)))
