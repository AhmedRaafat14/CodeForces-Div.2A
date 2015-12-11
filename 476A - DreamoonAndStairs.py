'''
Dreamoon wants to climb up a stair of n steps. He can climb 1 or 2 steps
at each move. Dreamoon wants the number of moves to be a
multiple of an integer m.

What is the minimal number of moves making him climb to the top of
the stairs that satisfies his condition?
============================
Input
The single line contains two space separated integers n, m
(0 < n ≤ 10000, 1 < m ≤ 10).
============================
Output
Print a single integer — the minimal number of moves being a multiple of m.
If there is no way he can climb satisfying condition print  - 1 instead.
============================
Sample test(s)

Input
10 2
Output
6

Input
3 5
Output
-1
'''

##              Running Time   ===>>> 62 ms

data = input().split()

N, M = int(data[0]), int(data[1])

divisable_by_M = []

if N == M:
    print(M)
else:
    '''
       collect all numbers between M and N divisable by M
       and store them in one array then get the mid of array
    '''
    for i in range(M, N):
        if i%M == 0:
            divisable_by_M.append(i)

    if len(divisable_by_M) == 0:
        print('-1')
    else:
        print(divisable_by_M[len(divisable_by_M)//2])
