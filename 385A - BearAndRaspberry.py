'''
The bear decided to store some raspberry for the winter.
He cunningly found out the price for a barrel of honey in
kilos of raspberry for each of the following n days.
According to the bear's data, on the i-th (1 ≤ i ≤ n) day,
the price for one barrel of honey is going to is xi kilos of raspberry.

Unfortunately, the bear has neither a honey barrel, nor the raspberry.
At the same time, the bear's got a friend who is ready to lend him a barrel
of honey for exactly one day for c kilograms of raspberry.
That's why the bear came up with a smart plan. He wants to choose
some day d (1 ≤ d < n), lent a barrel of honey and immediately
(on day d) sell it according to a daily exchange rate.
The next day (d + 1) the bear wants to buy a new barrel of honey according
to a daily exchange rate (as he's got some raspberry left from selling
the previous barrel) and immediately (on day d + 1) give his friend
the borrowed barrel of honey as well as c kilograms of raspberry for
renting the barrel.

The bear wants to execute his plan at most once and then hibernate. What maximum number of kilograms of raspberry can he earn? Note that if at some point of the plan the bear runs out of the raspberry, then he won't execute such a plan.
==============================
Input
The first line contains two space-separated integers,
n and c (2 ≤ n ≤ 100, 0 ≤ c ≤ 100), — the number of days and
the number of kilos of raspberry that the bear should give for
borrowing the barrel.

The second line contains n space-separated integers x1, x2, ..., xn
(0 ≤ xi ≤ 100), the price of a honey barrel on day i.
==============================
Output
Print a single integer — the answer to the problem.
==============================
Sample test(s)

Input
5 1
5 10 7 3 20
Output
3

Input
6 2
100 1 10 40 10 40
Output
97

Input
3 0
1 2 3
Output
0
'''

##          Running Time ===>>>  62 ms 

data = input().split()
N, C = int(data[0]), int(data[1])

barels_prices = input().split()

barels_prices = list(map(int, barels_prices))

max_price = []
for i in range(N-1):
    max_price.append(barels_prices[i] - barels_prices[i+1] - C)

if max(max_price) == abs(max(max_price)):
    print(max(max_price))
else:
    print('0')
