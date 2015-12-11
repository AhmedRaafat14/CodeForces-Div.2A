'''
Pashmak has fallen in love with an attractive girl called Parmida
since one year ago...

Today, Pashmak set up a meeting with his partner in a romantic garden.
Unfortunately, Pashmak has forgotten where the garden is.
But he remembers that the garden looks like a square with sides parallel
to the coordinate axes. He also remembers that there
is exactly one tree on each vertex of the square.
Now, Pashmak knows the position of only two of the trees.
Help him to find the position of two remaining ones.
================================
Input
The first line contains four space-separated x1, y1, x2, y2
( - 100 ≤ x1, y1, x2, y2 ≤ 100) integers,
where x1 and y1 are coordinates of
the first tree and x2 and y2 are coordinates of the second tree.
It's guaranteed that the given points are distinct.
================================
Output
If there is no solution to the problem, print -1.
Otherwise print four space-separated integers x3, y3, x4, y4
that correspond to the coordinates of the two other trees.
If there are several solutions you can output any of them.

Note that x3, y3, x4, y4 must be in the range
( - 1000 ≤ x3, y3, x4, y4 ≤ 1000).
================================
Sample test(s)

Input
0 0 0 1
Output
1 0 1 1
Input
0 0 1 1

Output
0 1 1 0
Input
0 0 1 2
Output
-1
'''

##              Running Time ===>>>  62 ms

data  = input().split()

X1, Y1, X2, Y2  =  int(data[0]), int(data[1]), int(data[2]), int(data[3])

X3, Y3, X4, Y4 = 0, 0, 0, 0

if X1 != X2 and Y1 != Y2 and abs(X2 - X1) != abs(Y2 - Y1):
    print('-1')
    exit
else:
    if X1 == X2:
        X3, Y3, X4, Y4 = X1 + abs(Y2 - Y1), Y1, X2 + abs(Y2 - Y1), Y2
    elif Y1 == Y2:
        X3, Y3, X4, Y4 = X1, Y1 + abs(X2 - X1), X2, Y2 + abs(X2 - X1)
    else:
        X3, Y3, X4, Y4 = X1, Y2, X2, Y1

    print(X3, Y3, X4, Y4)
