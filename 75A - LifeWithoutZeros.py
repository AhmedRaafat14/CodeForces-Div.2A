'''
Can you imagine our life if we removed all zeros from it?
For sure we will have many problems.

In this problem we will have a simple example
if we removed all zeros from our life, it's the addition operation.
Let's assume you are given this equation a + b = c,
where a and b are positive integers, and c is the sum of a and b.
Now let's remove all zeros from this equation.
Will the equation remain correct after removing all zeros?

For example if the equation is 101 + 102 = 203,
if we removed all zeros it will be 11 + 12 = 23
which is still a correct equation.

But if the equation is 105 + 106 = 211,
if we removed all zeros it will be 15 + 16 = 211
which is not a correct equation.
============================
Input
The input will consist of two lines, the first line will
contain the integer a, and the second line will contain
the integer b which are in the equation as described above
(1 ≤ a, b ≤ 109). There won't be any leading zeros in both.
The value of c should be calculated as c = a + b.
============================
Output
The output will be just one line, you should print "YES" if
the equation will remain correct after removing all zeros,
and print "NO" otherwise.
============================
Sample test(s)

Input
101
102
Output
YES

Input
105
106
Output
NO
'''

##              Running Time  ===>>>  124 ms

A = input()
B = input()

##      In first sum A +  in C and convert C to string to can reomve 0
C = str(int(A) + int(B))

##      Then Reomve all zeros from A, B and C
A = A.replace('0', '')
B = B.replace('0', '')
C = C.replace('0', '')

##      Then check if sum of A, B still equal to C so print YES
##      Otherwise, print NO
if int(A) + int(B)  == int(C):
    print('YES')
else:
    print('NO')
