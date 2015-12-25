'''
Vasya has recently found out what a digital root of a number is and he decided to share his knowledge with you.

Let's assume that S(n) is the sum of digits of number n,
for example, S(4098) = 4 + 0 + 9 + 8 = 21.
Then the digital root of number n equals to:

    -- dr(n) = S(n), if S(n) < 10;
    -- dr(n) = dr( S(n) ), if S(n) ≥ 10. 

For example, dr(4098)  =  dr(21)  =  3.

Vasya is afraid of large numbers, so the numbers he
works with are at most 101000. For all such numbers,
he has proved that dr(n)  =  S( S( S( S(n) ) ) ) (n ≤ 101000).

Now Vasya wants to quickly find numbers with the given digital root.
The problem is, he hasn't learned how to do that and he asked you to help him.
You task is, given numbers k and d, find the number consisting of exactly
k digits (the leading zeroes are not allowed), with digital root equal to d,
or else state that such number does not exist.
===================================
Input
The first line contains two integers k and d (1 ≤ k ≤ 1000; 0 ≤ d ≤ 9).
===================================
Output
In a single line print either any number that meets the requirements
(without the leading zeroes) or "No solution" (without the quotes),
if the corresponding number does not exist.

The chosen number must consist of exactly k digits.
We assume that number 0 doesn't contain any leading zeroes.
===================================
Sample test(s)

Input
4 4
Output
5881

Input
5 1
Output
36172

Input
1 0
Output
0
'''

##              Running Time  ===>>>  77 ms

data = input().split()

K, D = int(data[0]), int(data[1])

## if d == 0 so we have two states if k == 1 so solution will be 0
##                                 otherwise there's no solution
## otherwise, one of possible solution is product of d wih 10 powerd to
##            k-1
if D == 0:
    if K == 1:
        print('0')
    else:
        print('No solution')
else:
    print(D * (10 ** (K-1)))

            
