'''
Kevin Sun has just finished competing in Codeforces Round #334!
The round was 120 minutes long and featured five problems with maximum point
values of 500, 1000, 1500, 2000, and 2500, respectively.
Despite the challenging tasks, Kevin was uncowed and bulldozed through all
of them, distinguishing himself from the herd as the best cowmputer scientist
in all of Bovinia. Kevin knows his submission time for each problem,
the number of wrong submissions that he made on each problem,
and his total numbers of successful and unsuccessful hacks.
Because Codeforces scoring is complicated,
Kevin wants you to write a program to compute his final score.

Codeforces scores are computed as follows: If the maximum point value of
a problem is x, and Kevin submitted correctly at minute m but made w wrong
submissions, then his score on that problem is .
His total score is equal to the sum of his scores for each problem.
In addition, Kevin's total score gets increased by 100
points for each successful hack, but gets decreased by 50 points for
each unsuccessful hack.

All arithmetic operations are performed with absolute precision and no rounding.
It is guaranteed that Kevin's final score is an integer.
=================================
Input
The first line of the input contains five space-separated integers
m1, m2, m3, m4, m5, where mi (0 ≤ mi ≤ 119) is the time of Kevin's
last submission for problem i. His last submission is always correct
and gets accepted.
The second line contains five space-separated integers w1, w2, w3, w4, w5,
where wi (0 ≤ wi ≤ 10) is Kevin's number of wrong submissions on problem i.
The last line contains two space-separated integers hs and hu (0 ≤ hs, hu ≤ 20)
, denoting the Kevin's numbers of successful and unsuccessful hacks,
respectively.

Output
Print a single integer, the value of Kevin's final score.
=================================
Sample test(s)

Input
20 40 60 80 100
0 1 2 3 4
1 0
Output
4900

Input
119 119 119 119 119
0 0 0 0 0
10 0
Output
4930
'''

##              Running Time  ===>>>   62 ms

problems_times = input().split()
problems_times = list(map(int, problems_times))

problems_wrong = input().split()
problems_wrong = list(map(int, problems_wrong))

problems_hacks = input().split()
h1, h2  = int(problems_hacks[0]), int(problems_hacks[1])

total_score = 0
problems_scores = [500, 1000, 1500, 2000, 2500]
##      max(0.3*X, (1-(M/250))*(X-(50*W)))
##          X ==> max points for each problem
##          M ==> submit time for each problem
##          X ==> wrong submission for each problem
for i in range(0, len(problems_times)):
    Xi = problems_scores[i]
    Mi = problems_times[i]
    Wi = problems_wrong[i]
    score = max(0.3*Xi, (1-(Mi/250))*Xi-50*Wi)
    total_score += score
##          h1   ===> successful hacks number
##          h2   ===> unsuccessful hacks number
total_score += h1 * 100
total_score -= h2 * 50

print(int(total_score))



'''
s1 = max(0.3*500, (1-(20/250))*(500-(50*0)))

s2 = max(0.3*1000, (1-(40/250))*(1000-(50*1)))

s3 = max(0.3*1500, (1-(60/250))*(1500-(50*2)))

s4 = max(0.3*2000, (1-(80/250))*(2000-(50*3)))

s5 = max(0.3*2500, (1-(100/250))*(2500-(50*4)))

print((s1+s2+s3+s4+s5)+(1*100))
'''
