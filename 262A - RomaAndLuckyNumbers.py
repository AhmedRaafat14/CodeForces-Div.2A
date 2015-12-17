'''
Roma (a popular Russian name that means 'Roman') loves the Little Lvov
Elephant's lucky numbers.

Let us remind you that lucky numbers are positive integers whose decimal
representation only contains lucky digits 4 and 7.
For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Roma's got n positive integers. He wonders, how many of those
integers have not more than k lucky digits? Help him,
write the program that solves the problem.
================================
Input
The first line contains two integers n, k (1 ≤ n, k ≤ 100).
The second line contains n integers ai (1 ≤ ai ≤ 109) —
the numbers that Roma has.

The numbers in the lines are separated by single spaces.
================================
Output
In a single line print a single integer — the answer to the problem.
================================
Sample test(s)

Input
3 4
1 2 4
Output
3

Input
3 2
447 44 77
Output
2
'''

##              Running Time  ===>>> 156 ms

data = input().split()

N, K  =  int(data[0]), int(data[1])

numbers = input().split()

answer = 0
for i in range(N):
    if (numbers[i].count('4') + numbers[i].count('7')) <= K:
        answer += 1

print(answer)
