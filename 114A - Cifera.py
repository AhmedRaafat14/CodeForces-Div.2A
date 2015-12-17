'''
When Petya went to school, he got interested in large numbers and
what they were called in ancient times. For instance,
he learned that the Russian word "tma"
(which now means "too much to be counted")
used to stand for a thousand and "tma tmyschaya"
(which literally means "the tma of tmas") used to stand for a million.

Petya wanted to modernize the words we use for numbers and invented a
word petricium that represents number k. Moreover,
petricium la petricium stands for number k2, petricium la petricium
la petricium stands for k3 and so on. All numbers of this form are
called petriciumus cifera, and the number's importance is the number
of articles la in its title.

Petya's invention brought on a challenge that needed to be solved quickly:
does some number l belong to the set petriciumus cifera?
As Petya is a very busy schoolboy he needs to automate the process,
he asked you to solve it.
=================================
Input
The first input line contains integer number k,
the second line contains integer number l (2 ≤ k, l ≤ 231 - 1).
=================================
Output
You should print in the first line of the output "YES",
if the number belongs to the set petriciumus cifera and otherwise print "NO".
If the number belongs to the set, then print on the seconds line
the only number — the importance of number l.
=================================
Sample test(s)

Input
5
25
Output
YES
1

Input
3
8
Output
NO
'''
##              Running Time   ===>>> 92 ms

K = int(input())
L = int(input())


importance = 0
flag = 0
## on base 64 so loop from 1---64 (i = 1 to i < 65)
##  check if found the i which k^i == l so this is the solution
for i in range(1,65):
    if K**i == L:
        flag = 1
        importance = i
        break
if flag == 1:
    print('YES')
    print(importance-1)
else:
    print('NO')
