'''
Yaroslav has an array that consists of n integers.
In one second Yaroslav can swap two neighboring array elements.
Now Yaroslav is wondering if he can obtain an array where any
two neighboring elements would be distinct in a finite time.

Help Yaroslav.
=======================================
Input
The first line contains integer n (1 ≤ n ≤ 100)
— the number of elements in the array.
The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 1000)
— the array elements.
=======================================
Output
In the single line print "YES" (without the quotes)
if Yaroslav can obtain the array he needs, and "NO"
(without the quotes) otherwise.
=======================================
Sample test(s)

Input
1
1
Output
YES

Input
3
1 1 2
Output
YES

Input
4
7 7 7 7
Output
NO
'''

##             Running Time  ===>>>   124 ms

import math

N = int(input())

numbers = list(map(int, input().split()))

if all(e == numbers[0] for e in numbers) and N != 1:
    print('NO')
elif N == 1:
    print('YES')
else:
    set_of_numbers = list(set(numbers))

    counter = [None] * len(set_of_numbers)
    for i in range(len(set_of_numbers)):
        counter[i] = numbers.count(set_of_numbers[i])

    if max(counter) > math.ceil(N/2):
        print('NO')
    else:
        print('YES')
'''

import math

N = int(input())

numbers = list(map(int, input().split()))


set_of_numbers = list(set(numbers))

counter = [None] * len(set_of_numbers)
for i in range(len(set_of_numbers)):
    counter[i] = numbers.count(set_of_numbers[i])

if max(counter) > math.ceil(N/2):
    print('NO')
else:
    print('YES')

'''
