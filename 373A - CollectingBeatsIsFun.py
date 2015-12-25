'''
Cucumber boy is fan of Kyubeat, a famous music game.

Kyubeat has 16 panels for playing arranged in 4 × 4 table.
When a panel lights up, he has to press that panel.

Each panel has a timing to press (the preffered time when a
player should press it), and Cucumber boy is able to press
at most k panels in a time with his one hand.
Cucumber boy is trying to press all panels in perfect timing,
that is he wants to press each panel exactly in its preffered time.
If he cannot press the panels with his two hands in perfect timing,
his challenge to press all the panels in perfect timing will fail.

You are given one scene of Kyubeat's panel from the music Cucumber boy
is trying. Tell him is he able to press all the panels in perfect timing.
====================================
Input
The first line contains a single integer k (1 ≤ k ≤ 5)
— the number of panels Cucumber boy can press with his one hand.

Next 4 lines contain 4 characters each (digits from 1 to 9, or period)
— table of panels. If a digit i was written on the panel,
it means the boy has to press that panel in time i.
If period was written on the panel, he doesn't have to press that panel.
====================================
Output
Output "YES" (without quotes), if he is able to press all
the panels in perfect timing. If not, output "NO" (without quotes).
====================================
Sample test(s)

Input
1
.135
1247
3468
5789
Output
YES

Input
5
..1.
1111
..1.
..1.
Output
YES

Input
1
....
12.1
.2..
.2..
Output
NO
'''

##              Running Time   ===>>>    62 ms

K = int(input())

panels = [None] * 4
for i in range(4):
    panels[i] = input()


all_hands = K * 2

digits_lis = [0] * 9

## we just count all 9 digits for each row and see if there's any one of them
##  its count is cross over the number of panels which two hands can press on it
##   so we answer NO otherwise all of them is less than # of panels for 2 hands
##   so we answer YES
for i in range(4):
    digits_lis[0] += panels[i].count('1')
    digits_lis[1] += panels[i].count('2')
    digits_lis[2] += panels[i].count('3')
    digits_lis[3] += panels[i].count('4')
    digits_lis[4] += panels[i].count('5')
    digits_lis[5] += panels[i].count('6')
    digits_lis[6] += panels[i].count('7')
    digits_lis[7] += panels[i].count('8')
    digits_lis[8] += panels[i].count('9')

if max(digits_lis) > all_hands:
    print('NO')
else:
    print('YES')
