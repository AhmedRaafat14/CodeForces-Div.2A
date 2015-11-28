'''
After seeing the "ALL YOUR BASE ARE BELONG TO US" meme for the first time,
numbers X and Y realised that they have different bases,
which complicated their relations.

You're given a number X represented in base bx and a number Y represented in
base by. Compare those two numbers.
====================================
Input
The first line of the input contains two space-separated integers n and bx
(1 ≤ n ≤ 10, 2 ≤ bx ≤ 40), where n is the number of digits in the bx-based
representation of X.

The second line contains n space-separated integers x1, x2, ..., xn
(0 ≤ xi < bx) — the digits of X. They are given in the order from the
most significant digit to the least significant one.

The following two lines describe Y in the same way: the third line
contains two space-separated integers m and by (1 ≤ m ≤ 10, 2 ≤ by ≤ 40,
bx ≠ by), where m is the number of digits in the by-based representation of Y,
and the fourth line contains m space-separated integers y1, y2, ..., ym
(0 ≤ yi < by) — the digits of Y.

There will be no leading zeroes. Both X and Y will be positive.
All digits of both numbers are given in the standard decimal numeral system.
====================================
Output
Output a single character (quotes for clarity):

    '<' if X < Y
    '>' if X > Y
    '=' if X = Y 
====================================
Sample test(s)

Input
6 2
1 0 1 1 1 1
2 10
4 7
Output
=

Input
3 3
1 0 2
2 5
2 4
Output
<

Input
7 16
15 15 4 0 0 7 10
7 9
4 8 0 3 1 5 0
Output
>


link ==> http://codeforces.com/problemset/problem/602/A
'''

##                  Running Time    ===>>   62 ms

##   n and bx (1 ≤ n ≤ 10, 2 ≤ bx ≤ 40),
##      where n is the number of digits in the bx-based representation of X. 
X_N_Bx = raw_input().split()
N, Bx = int(X_N_Bx[0]), int(X_N_Bx[1])
##  n space-separated integers x1, x2, ..., xn (0 ≤ xi < bx) — the digits of X
digits_X = raw_input().split()
digits_X = map(int, digits_X)

## m and by (1 ≤ m ≤ 10, 2 ≤ by ≤ 40, bx ≠ by),
##     where m is the number of digits in the by-based representation of Y
Y_M_By = raw_input().split()
M, By = int(Y_M_By[0]), int(Y_M_By[1])
##  m space-separated integers y1, y2, ..., ym (0 ≤ yi < by) — the digits of Y.
digits_Y = raw_input().split()
digits_Y = map(int, digits_Y)

X_base_ten = 0
Y_base_ten = 0

X_size = 0
Y_size = 0

X_idx, X_power = len(digits_X)-1, 0
Y_idx, Y_power = len(digits_Y)-1, 0

## Convert any given base to base 10 and compare the results :)
while True:
    if X_size == len(digits_X) and Y_size == len(digits_Y):
        break
    if X_size < len(digits_X):
        X_base_ten += digits_X[X_idx] * (Bx**X_power)
        X_idx   -= 1
        X_power += 1
        X_size  += 1
    if By != 10:
        if Y_size < len(digits_Y):
            Y_base_ten += digits_Y[Y_idx] * (By**Y_power)
            Y_idx   -= 1
            Y_power += 1
            Y_size  += 1
    elif By == 10:
        Y_base_ten = int(''.join(map(str, digits_Y)))
        Y_size = len(digits_Y)


if X_base_ten < Y_base_ten:
    print('<')
if X_base_ten > Y_base_ten:
    print('>')
if X_base_ten == Y_base_ten:
    print('=')
