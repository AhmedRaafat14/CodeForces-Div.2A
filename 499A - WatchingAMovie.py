'''
You have decided to watch the best moments of some movie.
There are two buttons on your player:

    -- Watch the current minute of the movie. By pressing this button,
       you watch the current minute of the movie and the player automatically
       proceeds to the next minute of the movie.
    -- Skip exactly x minutes of the movie (x is some fixed positive integer).
       If the player is now at the t-th minute of the movie,
       then as a result of pressing this button, it proceeds to
       the minute (t + x). 

Initially the movie is turned on in the player on the first minute,
and you want to watch exactly n best moments of the movie,
the i-th best moment starts at the li-th minute and ends at
the ri-th minute (more formally, the i-th best moment consists of minutes:
li, li + 1, ..., ri).

Determine, what is the minimum number of minutes of the movie you
have to watch if you want to watch all the best moments?
====================================
Input
The first line contains two space-separated integers n, x
(1 ≤ n ≤ 50, 1 ≤ x ≤ 105) — the number of the best moments of
the movie and the value of x for the second button.

The following n lines contain the descriptions of the best moments of
the movie, the i-th line of the description contains two integers
separated by a space li, ri (1 ≤ li ≤ ri ≤ 105).

It is guaranteed that for all integers i from 2 to n the following
condition holds: ri - 1 < li.
====================================
Output
Output a single number — the answer to the problem.
====================================
Sample test(s)

Input
2 3
5 6
10 12
Output
6

Input
1 1
1 100000
Output
100000
'''

##              Running Time ====>>>>   108 ms

data = input().split()

N, X = int(data[0]), int(data[1])

best = [None] * N
for i in range(N):
    best[i] = list(map(int, input().split()))

minuts = 1
counter = 0
##   For all minuts+X less than th Li so add X to minuts
##   If we found minuts+X is greater than Li and minuts less than Li
##      For all minuts less than Ri we just move one minute and count 1
for i in range(N):
    while minuts+X <= best[i][0]:
        minuts += X
    if minuts <= best[i][0]:
        while minuts <= best[i][1]:
            counter += 1
            minuts += 1
            

print(counter)

