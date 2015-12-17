'''
Misha and Vasya participated in a Codeforces contest.
Unfortunately, each of them solved only one problem,
though successfully submitted it at the first attempt.
Misha solved the problem that costs a points and Vasya
solved the problem that costs b points.
Besides, Misha submitted the problem c minutes after
the contest started and Vasya submitted the problem d minutes after
the contest started. As you know, on Codeforces the cost of a problem
reduces as a round continues.
That is, if you submit a problem that costs p points t minutes after
the contest started, you max((3*p)/10, p - (p/250) * t) get points.

Misha and Vasya are having an argument trying to find
out who got more points. Help them to find out the truth.
================================
Input
The first line contains four integers a, b, c, d
(250 ≤ a, b ≤ 3500, 0 ≤ c, d ≤ 180).

It is guaranteed that numbers a and b
are divisible by 250 (just like on any real Codeforces round).
================================
Output
Output on a single line:
"Misha" (without the quotes), if Misha got more points than Vasya.
"Vasya" (without the quotes), if Vasya got more points than Misha.
"Tie" (without the quotes), if both of them got the same number of points.
================================
Sample test(s)

Input
500 1000 20 30
Output
Vasya

Input
1000 1000 1 1
Output
Tie

Input
1500 1000 176 177
Output
Misha
'''

##              Running Time ===>>> 62 ms

data = input().split()

A, B, C, D = int(data[0]), int(data[1]), int(data[2]), int(data[3])

misha_scores = max((3*A)/10, A - (A/250) * C)
vasya_scores = max((3*B)/10, B - (B/250) * D)

if misha_scores > vasya_scores:
    print('Misha')
elif misha_scores < vasya_scores:
    print('Vasya')
else:
    print('Tie')
