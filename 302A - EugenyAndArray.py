'''
Eugeny has array a = a1, a2, ..., an, consisting of n integers.
Each integer ai equals to -1, or to 1. Also, he has m queries:

    -- Query number i is given as a pair of integers li, ri (1 ≤ li ≤ ri ≤ n).
    -- The response to the query will be integer 1,
       if the elements of array a can be rearranged so as
       the sum ali + ali + 1 + ... + ari = 0, otherwise the response
       to the query will be integer 0. 

Help Eugeny, answer all his queries.
==================================
Input
The first line contains integers n and m (1 ≤ n, m ≤ 2·105).
The second line contains n integers a1, a2, ..., an (ai = -1, 1).
Next m lines contain Eugene's queries. The i-th line contains integers
li, ri (1 ≤ li ≤ ri ≤ n).
==================================
Output
Print m integers — the responses to Eugene's queries in
the order they occur in the input.
==================================
Sample test(s)

Input
2 3
1 -1
1 1
1 2
2 2
Output
0
1
0

Input
5 5
-1 1 1 1 -1
1 1
2 3
3 5
2 5
1 5
Output
0
1
0
1
0
'''

##          Running Time  ===>>> 780 ms

N, M = map(int, input().split())

A = input().split()

count_one = A.count('1')

solution = []

queries = []
for i in range(M):
    Li, Ri = map(int, input().split())
    if ( (Ri-Li+1)%2 == 0 and
         (Ri-Li+1)//2 <= min(count_one, N-count_one)):
        solution.append('1')
        continue
    else:
        solution.append('0')

print('\n'.join(solution))
