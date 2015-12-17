'''
A permutation is a sequence of integers p1, p2, ..., pn,
consisting of n distinct positive integers, each of them doesn't exceed n.
Let's denote the i-th element of permutation p as pi. We'll call number n
the size of permutation p1, p2, ..., pn.

Nickolas adores permutations. He likes some permutations more than the others.
He calls such permutations perfect. A perfect permutation is such permutation
p that for any i (1 ≤ i ≤ n) (n is the permutation size)
the following equations hold ppi = i and pi ≠ i.
Nickolas asks you to print any perfect permutation of size n for the given n.
===============================
Input
A single line contains a single integer n (1 ≤ n ≤ 100) —
the permutation size.
===============================
Output
If a perfect permutation of size n doesn't exist, print a single integer -1.
Otherwise print n distinct integers from 1 to n, p1, p2, ..., pn —
permutation p, that is perfect. Separate printed numbers by whitespaces.
===============================
Sample test(s)

Input
1
Output
-1

Input
2
Output
2 1

Input
4
Output
2 1 4 3
'''

##              Running Time  ===>>>  154 ms

N = int(input())

'''
    check if the given number is odd so there's no solution follow above
    rules  this rule:
             A perfect permutation is such permutation
              p that for any i (1 ≤ i ≤ n) (n is the permutation size)
                 the following equations hold ppi = i and pi ≠ i.
    otherwise, if its even so we loop through the N and for each integer check if
               current i even or odd if its even so put in i-1 (ex. i=4, p[3])
               we put in it even number which equal to i-1 (ex. i=4 p[3]=3)
               if its odd we put iin i - 1 the value of i + 1 which it will
               be even (ex. i=3 p[2] = 4)
'''
if N%2 != 0:
    print('-1')
    exit
else:
    permute = [0] * N
    for i in range(1, N+1):
        if i%2 == 0:
            permute[i-1] = i - 1
            continue
        permute[i-1] = i + 1
    
    print(" ".join(map(str, permute)))
