'''
Mike is trying rock climbing but he is awful at it.

There are n holds on the wall, i-th hold is at height ai off the ground.
Besides, let the sequence ai increase, that is,
ai < ai + 1 for all i from 1 to n - 1;
we will call such sequence a track.
Mike thinks that the track a1, ..., an has difficulty .
In other words, difficulty equals
the maximum distance between two holds that are adjacent in height.

Today Mike decided to cover the track with holds hanging on heights
a1, ..., an. To make the problem harder, Mike decided to remove one hold,
that is, remove one element of the sequence (for example,
if we take the sequence (1, 2, 3, 4, 5) and
remove the third element from it, we obtain the sequence (1, 2, 4, 5)).
However, as Mike is awful at climbing, he wants the final difficulty
(i.e. the maximum difference of heights between adjacent
holds after removing the hold) to be as small as possible among
all possible options of removing a hold. The first and last holds
must stay at their positions.

Help Mike determine the minimum difficulty of the track after removing one hold.
===========================
Input
The first line contains a single integer n (3 ≤ n ≤ 100) —
the number of holds.

The next line contains n space-separated integers ai (1 ≤ ai ≤ 1000),
where ai is the height where the hold number i hangs.
The sequence ai is increasing
(i.e. each element except for the first one is strictly larger than
the previous one).
===========================
Output
Print a single number —
the minimum difficulty of the track after removing a single hold.
===========================
Sample test(s)

Input
3
1 4 6
Output
5

Input
5
1 2 3 4 5
Output
2

Input
5
1 2 3 7 8
Output
4
'''

##              Running Time ===>>>   62 ms

N = int(input())

holds = list(map(int, input().split()))
holds_diff = []
for i in range(1, N-1):
    max_diff = []
    holds_after_remove = holds[:i] + holds[i+1:]
    for j in range(len(holds_after_remove) - 1):
        max_diff.append(holds_after_remove[j+1] - holds_after_remove[j])

    holds_diff.append(max(max_diff))

print(min(holds_diff))
    
