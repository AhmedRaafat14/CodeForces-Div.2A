'''
Bob is preparing to pass IQ test. The most frequent task in this
test is to find out which one of the given n numbers differs from
the others. Bob observed that one number usually differs from the
others in evenness. Help Bob — to check his answers, he needs a program
that among the given n numbers finds one that is different in evenness.
============================
Input
The first line contains integer n (3 ≤ n ≤ 100) —
amount of numbers in the task.
The second line contains n space-separated natural numbers,
not exceeding 100. It is guaranteed,
that exactly one of these numbers differs from the others in evenness.
============================
Output
Output index of number that differs from the others in evenness.
Numbers are numbered from 1 in the input order.
============================
Sample test(s)

Input
5
2 4 7 8 10
Output
3

Input
4
1 2 1 1
Output
2
'''
N = int(input())

numbers = input().split()
numbers = list(map(int, numbers))

even = []
odd  = []

for i in range(N):
    if numbers[i]%2 == 0:
        even.append(i+1)
        continue
    odd.append(i+1)

if len(even) == 1:
    print(even[0])
    exit
if len(odd) == 1:
    print(odd[0])
    exit
