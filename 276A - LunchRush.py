'''
Having written another programming contest, three Rabbits decided to
grab some lunch. The coach gave the team exactly k time units for
the lunch break.

The Rabbits have a list of n restaurants to lunch in: the i-th restaurant
is characterized by two integers fi and ti. Value ti shows the time
the Rabbits need to lunch in the i-th restaurant.
If time ti exceeds the time k that the coach has given for
the lunch break, then the Rabbits' joy from lunching in
this restaurant will equal fi - (ti - k). Otherwise,
the Rabbits get exactly fi units of joy.

Your task is to find the value of the maximum joy the Rabbits
can get from the lunch, depending on the restaurant.
The Rabbits must choose exactly one restaurant to lunch in.
Note that the joy value isn't necessarily a positive value.
==================================
Input
The first line contains two space-separated integers —
n (1 ≤ n ≤ 104) and k (1 ≤ k ≤ 109) — the number of restaurants in
the Rabbits' list and the time the coach has given them to lunch,
correspondingly. Each of the next n lines contains
two space-separated integers — fi (1 ≤ fi ≤ 109) and ti (1 ≤ ti ≤ 109) —
the characteristics of the i-th restaurant.
==================================
Output
In a single line print a single integer — the maximum joy value that
the Rabbits will get from the lunch.
==================================
Sample test(s)

Input
2 5
3 3
4 5
Output
4

Input
4 6
5 8
3 6
2 3
2 2
Output
3

Input
1 5
1 7
Output
-1
'''
##          Running Time  ====>>>>  218 ms

data = input().split()
N, K = int(data[0]), int(data[1])

resturants = [None] * N
for i in range(N):
    tmp_in = input().split()
    resturants[i] = list(map(int, tmp_in))

joy_li = []
for i in range(N):
    current_rest = resturants[i]
    if current_rest[1] <= K:
        joy_li.append(current_rest[0])
        continue
    else:
        joy_li.append(current_rest[0] - (current_rest[1] - K))
        continue

print(max(joy_li))
