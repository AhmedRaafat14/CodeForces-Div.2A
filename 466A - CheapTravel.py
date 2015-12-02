'''
Ann has recently started commuting by subway.
We know that a one ride subway ticket costs a rubles.
Besides, Ann found out that she can buy a special ticket for m rides
(she can buy it several times). It costs b rubles. Ann did the math;
she will need to use subway n times.
Help Ann, tell her what is the minimum sum of money she
will have to spend to make n rides?
=================================
Input
The single line contains four space-separated integers n, m, a, b
(1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned,
the number of rides covered by the m ride ticket,
the price of a one ride ticket and the price of an m ride ticket.
=================================
Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.
=================================
Sample test(s)

Input
6 2 1 2
Output
6

Input
5 2 2 3
Output
8
'''

##                      Running Time ===> 62 ms

data = input().split()

N, M, A, B = int(data[0]), int(data[1]), int(data[2]), int(data[3])

if (M*A) <= B:
    print(N*A)
else:
    print((N//M)*B + min((N%M)*A, B))

