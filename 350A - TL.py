'''
Valera wanted to prepare a Codesecrof round.
He's already got one problem and he wants to set a time limit (TL) on it.

Valera has written n correct solutions. For each correct solution,
he knows its running time (in seconds).
Valera has also wrote m wrong solutions and for each wrong solution
he knows its running time (in seconds).

Let's suppose that Valera will set v seconds TL in the problem.
Then we can say that a solution passes the system testing if
its running time is at most v seconds. We can also say that a solution passes
the system testing with some "extra" time if for its running time, a seconds,
an inequality 2a ≤ v holds.

As a result, Valera decided to set v seconds TL,
that the following conditions are met:

    -- v is a positive integer;
    -- all correct solutions pass the system testing;
    -- at least one correct solution passes the system testing with some "extra" time;
    -- all wrong solutions do not pass the system testing;
    -- value v is minimum among all TLs, for which points 1, 2, 3, 4 hold. 

Help Valera and find the most suitable TL or else state that such
TL doesn't exist.
================================
Input
The first line contains two integers n, m (1 ≤ n, m ≤ 100).
The second line contains n space-separated positive integers a1, a2, ..., an
(1 ≤ ai ≤ 100) — the running time of each of the n correct solutions in seconds.
The third line contains m space-separated positive integers b1, b2, ..., bm
(1 ≤ bi ≤ 100) — the running time of each of m wrong solutions in seconds.
================================
Output
If there is a valid TL value, print it. Otherwise, print -1.
================================
Sample test(s)

Input
3 6
4 5 2
8 9 6 10 7 11
Output
5

Input
3 1
3 4 5
6
Output
-1
'''

##          Running Time ===>>> 124 ms

## Read Data
data = input().split()
N, M = int(data[0]), int(data[1])

correct = list(map(int, input().split()))
wrong = list(map(int, input().split()))

## select minmum wrong answer time
min_wrong_time = min(wrong)
## collect all possible solutions
possible_TLs = [i+1 for i in range(min_wrong_time-1)]

## collect TLS which correct answers can pass
TL_solutions = []
for i in range(len(possible_TLs)):
    if all(e <= possible_TLs[i] for e in correct):
        TL_solutions.append(possible_TLs[i])
## if there's no possible solutions so print -1
if len(TL_solutions) == 0:
    print('-1')
    exit()
else:
    ## Otherwise, collect all solutions which have at least
    ##            one solution satisfy this condition 2*a <= v
    ##        then check if there's no solutions print -1 otherwise print
    ##          The minimum one
    TLs = []
    for i in range(len(TL_solutions)):
        if any(2*e <= TL_solutions[i] for e in correct):
            TLs.append(TL_solutions[i])
    if len(TLs) == 0:
        print('-1')
        exit()
    else:
        print(min(TLs))

'''
##          Running Time ===>>> 124 ms

data = input().split()
N, M = int(data[0]), int(data[1])

correct = list(map(int, input().split()))
wrong = list(map(int, input().split()))

V = min(correct)
P = max(correct)
C = min(wrong)

if max(2 * V, P) < C:
    print(max(2 * V, P))
else:
    print('-1')
'''
