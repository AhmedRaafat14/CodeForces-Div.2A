'''
Valera had two bags of potatoes, the first of these bags contains
x (x ≥ 1) potatoes, and the second — y (y ≥ 1) potatoes.
Valera — very scattered boy, so the first bag of potatoes
(it contains x potatoes) Valera lost. Valera remembers that
the total amount of potatoes (x + y) in the two bags,
firstly, was not gerater than n, and, secondly, was divisible by k.

Help Valera to determine how many potatoes could be in the first bag.
Print all such possible numbers in ascending order.
============================
Input
The first line of input contains three integers y, k, n (1 ≤ y, k, n ≤ 109;  
≤ 105).
============================
Output
Print the list of whitespace-separated integers — all possible values of
x in ascending order. You should print each possible value of x exactly once.

If there are no such values of x print a single integer -1.
============================
Sample test(s)

Input
10 1 10
Output
-1

Input
10 6 40
Output
2 8 14 20 26
'''

##          Running Time   ===>>>   248 ms

data = input().split()

Y, K, N = int(data[0]), int(data[1]), int(data[2])

answer = []
##  So simple solution we just start count from K to N
##  and when we found i greater than Y value we just get one of answers will be
##      i - Y
##  and then increase i by K
i = K
while i <= N:
    if i > Y:
        answer.append(i - Y)
    i += K

if len(answer) == 0:
    print('-1')
else:
    print(" ".join(map(str, answer)))
