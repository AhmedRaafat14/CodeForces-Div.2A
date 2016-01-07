'''
Sean is trying to save a large file to a USB flash drive.
He has n USB flash drives with capacities equal to a1, a2, ..., an megabytes.
The file size is equal to m megabytes.

Find the minimum number of USB flash drives needed to write Sean's file,
if he can split the file between drives.
============================
Input
The first line contains positive integer n (1 ≤ n ≤ 100)
— the number of USB flash drives.

The second line contains positive integer m (1 ≤ m ≤ 105)
— the size of Sean's file.

Each of the next n lines contains positive integer ai (1 ≤ ai ≤ 1000)
— the sizes of USB flash drives in megabytes.

It is guaranteed that the answer exists, i. e.
the sum of all ai is not less than m.
============================
Output
Print the minimum number of USB flash drives to write Sean's file,
if he can split the file between drives.
============================
Sample test(s)

Input
3
5
2
1
3
Output
2

Input
3
6
2
3
2
Output
3

Input
2
5
5
10
Output
1
'''

##              Running Time  ===>>>   61 ms

N = int(input())
M = int(input())

A = []
for i in range(N):
    A.append(int(input()))

if any(e >= M for e in A):
    print('1')
else:
    answer = 0
    A = sorted(A, reverse=True)
    i = 0
    while M > 0:
        M -= A[i]
        answer += 1
        i += 1

    print(answer)
