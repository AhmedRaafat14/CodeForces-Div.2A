'''
Fox Ciel is playing a game with numbers now.

Ciel has n positive integers: x1, x2, ..., xn.
She can do the following operation as many times as needed:
select two different indexes i and j such that xi > xj hold,
and then apply assignment xi = xi - xj. The goal is to make
the sum of all numbers as small as possible.

Please help Ciel to find this minimal sum.
=====================================
Input
The first line contains an integer n (2 ≤ n ≤ 100).
Then the second line contains n integers: x1, x2, ..., xn (1 ≤ xi ≤ 100).
=====================================
Output
Output a single integer — the required minimal sum.
=====================================
Sample test(s)

Input
2
1 2
Output
2

Input
3
2 4 6
Output
6

Input
2
12 18
Output
12

Input
5
45 12 27 30 18
Output
15
'''

##              Running Time ===>>> 171 ms

N = int(input())

fox_numbers = list(map(int, input().split()))

##  Best case all numbers are equal so print sum of them
if list(set(fox_numbers)) == 1:
    print(sum(fox_numbers))
else:
    ##  Otherwise, we loop through them till all of them be equal
    answer = []
    times = 0
    '''
        ##    loop forever and break just when answer have same values
        ##  else go to loops and through i, j select the j index which
        ##      it's value smaller than i-th value and when get out loop check
        ##       if there's selected index so append Xi - Xidx (idx = j)
        ##       otherwise append the i-th value cuz its smaller one
        ##  out loop assign 1 to times var and reapeat if first condition
        ##  evaluate "break" and print sum of answer array
        ##  otherwise, assign 0 to times var and copy answer list to numbers
        ##          and re-assign answer list to empty one and do prev steps again
    '''
    while True:
        if len(answer) > 1 and all(e == answer[0] for e in answer):
            break
        elif times == 1:
            times = 0
            fox_numbers = answer.copy()
            answer = []
        for i in range(N):
            idx = -1
            for j in range(N):
                if i == j:
                    continue
                if fox_numbers[i] > fox_numbers[j]:
                    idx = j
            if idx > -1:
                answer.append(fox_numbers[i] - fox_numbers[idx])
            else:
                answer.append(fox_numbers[i])
        times = 1

    print(sum(answer))
