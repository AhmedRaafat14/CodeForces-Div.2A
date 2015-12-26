'''
Little Vasya went to the supermarket to get some groceries.
He walked about the supermarket for a long time and got a basket
full of products. Now he needs to choose the cashier to pay for the products.

There are n cashiers at the exit from the supermarket.
At the moment the queue for the i-th cashier already has ki people.
The j-th person standing in the queue to the i-th cashier has mi, 
j items in the basket. Vasya knows that:

    -- the cashier needs 5 seconds to scan one item;
    -- after the cashier scans each item of some customer,
         he needs 15 seconds to take the customer's money
         and give him the change. 

Of course, Vasya wants to select a queue so that he can leave
the supermarket as soon as possible. Help him write a program
that displays the minimum number of seconds after which
Vasya can get to one of the cashiers.
============================
Input
The first line contains integer n (1 ≤ n ≤ 100)
— the number of cashes in the shop.
The second line contains n space-separated integers:
k1, k2, ..., kn (1 ≤ ki ≤ 100), where ki is the number
of people in the queue to the i-th cashier.

The i-th of the next n lines contains ki space-separated integers:
mi, 1, mi, 2, ..., mi, ki (1 ≤ mi, j ≤ 100) — the number of products
the j-th person in the queue for the i-th cash has.
============================
Output
Print a single integer
— the minimum number of seconds Vasya needs to get to the cashier.
============================
Sample test(s)

Input
1
1
1
Output
20

Input
4
1 4 3 2
100
1 2 2 3
1 9 1
7 8
Output
100
'''

##              Running Time  ===>>>  62 ms

N = int(input())

cashiers = []
K_unused = input().split()
for i in range(N):
    qu_sum = 0
    tmp = list(map(int, input().split()))
    queue = len(tmp)
    for e in tmp:
        qu_sum += (e*5) + 15
    cashiers.append(qu_sum)

print(min(cashiers))
