'''
Being a nonconformist, Volodya is displeased with the current state of things,
particularly with the order of natural numbers (natural number is positive
integer number). He is determined to rearrange them.
But there are too many natural numbers, so Volodya decided to start with
the first n. He writes down the following sequence of numbers:
firstly all odd integers from 1 to n (in ascending order),
then all even integers from 1 to n (also in ascending order).
Help our hero to find out which number will stand at the position number k.
============================
Input
The only line of input contains integers n and k (1 ≤ k ≤ n ≤ 1012).

Please, do not use the %lld specifier to read or write 64-bit integers in C++.
It is preferred to use the cin, cout streams or the %I64d specifier.
============================
Output
Print the number that will stand at the position number k after
Volodya's manipulations.
============================
Sample test(s)

Input
10 3
Output
5

Input
7 7
Output
6
'''
##              Running Time  ====>>>   122 ms

import math

data = input().split()

N, K = int(data[0]), int(data[1])

'''
We have here Two main cases for Odd and Even:
      Case #1:
            if the wanted number K larger than or equal ceil(N/2)
            this means user need an 'ODD' number which places
            in the first half so we get it by equation:
                       K + (K - 1)
    Case #2:
            if the wanted number K smaller than ceil(N/2)
            this means user need an 'EVEN' number which places
            in the second half... in this case we have
            three other cases as described:
                 1- if the wanted number K equal to amount of numbes N
                    so will just reduce the K by 1 to get last one:
                        K - 1
                 2- if the (N is odd and K is even) or (both of them are odd)
                    we get the wanted number by this equation:
                        (K - (N - K)) - 1
                 3- if both of them even will get number by this equation:
                        (K - (N - K))
'''
if K <= math.ceil(N/2):
    print(K+(K-1))
else:
    if K == N and K%2 != 0:
        print(K-1)
    elif (N%2 != 0 and K%2 == 0) or (N%2 != 0 and K%2 != 0):
        print((K-(N-K))-1)
    else:
        print((K-(N-K)))


