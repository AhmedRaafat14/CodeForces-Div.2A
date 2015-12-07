'''
Kirito is stuck on a level of the MMORPG he is playing now.
To move on in the game, he's got to defeat all n dragons
that live on this level. Kirito and the dragons have strength,
which is represented by an integer. In the duel between two opponents
the duel's outcome is determined by their strength.
Initially, Kirito's strength equals s.

If Kirito starts duelling with the i-th (1 ≤ i ≤ n) dragon and
Kirito's strength is not greater than the dragon's strength xi,
then Kirito loses the duel and dies. But if Kirito's strength is
greater than the dragon's strength, then he defeats the dragon and
gets a bonus strength increase by yi.

Kirito can fight the dragons in any order. Determine whether
he can move on to the next level of the game, that is,
defeat all dragons without a single loss.
===============================
Input
The first line contains two space-separated integers s and n
(1 ≤ s ≤ 104, 1 ≤ n ≤ 103). Then n lines follow:
the i-th line contains space-separated integers xi and yi
(1 ≤ xi ≤ 104, 0 ≤ yi ≤ 104) — the i-th dragon's strength and
the bonus for defeating it.
===============================
Output
On a single line print "YES" (without the quotes),
if Kirito can move on to the next level and print "NO"
(without the quotes), if he can't.
===============================
Sample test(s)

Input
2 2
1 99
100 0
Output
YES

Input
10 1
100 100
Output
NO
'''
##              Running Time   ====>>>   124 ms

data = input().split()

S, N  =   int(data[0]), int(data[1])

Nth_X_Y = [[0, 0]]* N

for i in range(0, N):
    tmp = input().split()
    Nth_X_Y[i] = list(map(int, tmp))

counter  = 0

Nth_X_Y = sorted(Nth_X_Y)

'''
After sorting the array which have dragons strength and bonues
all what we can do is loop through it all dragons whose its strength less than
Kirito strength add its bonus to him and count '1' till the end of array or
till we find a dragon its strength is greater than him break
and check if counter equal to the N so kirito win and move up
otherwise he lose
'''
for i in range(0, N):
    if S > Nth_X_Y[i][0]:
        S += Nth_X_Y[i][1]
        counter += 1
        continue
    else:
        break

if counter == N:
    print('YES')
else:
    print('NO')
