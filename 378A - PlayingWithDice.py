'''
Two players are playing a game. First each of them writes an
integer from 1 to 6, and then a dice is thrown.
The player whose written number got closer to
the number on the dice wins. If both payers have
the same difference, it's a draw.

The first player wrote number a, the second player wrote number b.
How many ways to throw a dice are there, at which the first player wins,
or there is a draw, or the second player wins?
===============================
Input
The single line contains two integers a and b (1 ≤ a, b ≤ 6) —
the numbers written on the paper by the first and second player,
correspondingly.
===============================
Output
Print three integers: the number of ways to throw the dice at
which the first player wins, the game ends with a draw or
the second player wins, correspondingly.
===============================
Sample test(s)

Input
2 5
Output
3 0 3

Input
2 4
Output
2 1 3
'''

##              Running Time  ===>>>  77 ms

data  = input().split()

A, B = int(data[0]), int(data[1])

A_wins = 0
B_wins = 0
draw = 0

for i in range(1, 7):
    if abs(A - i) < abs(B - i):
        A_wins += 1
        continue
    if abs(B - i) < abs(A - i):
        B_wins += 1
        continue
    else:
        draw += 1
        continue

print(A_wins, draw, B_wins)
