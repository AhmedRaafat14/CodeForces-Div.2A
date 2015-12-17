'''
One day Vasya painted a Cartesian coordinate system on a piece of
paper and marked some set of points (x1, y1), (x2, y2), ..., (xn, yn).
Let's define neighbors for some fixed point from the given set (x, y):

    -- point (x', y') is (x, y)'s right neighbor, if x' > x and y' = y
    -- point (x', y') is (x, y)'s left neighbor, if x' < x and y' = y
    -- point (x', y') is (x, y)'s lower neighbor, if x' = x and y' < y
    -- point (x', y') is (x, y)'s upper neighbor, if x' = x and y' > y 

We'll consider point (x, y) from the given set supercentral,
if it has at least one upper, at least one lower,
at least one left and at least one right neighbor among this set's points.

Vasya marked quite many points on the paper.
Analyzing the picture manually is rather a challenge,
so Vasya asked you to help him.
Your task is to find the number of supercentral points in the given set.
===============================
Input
The first input line contains the only integer n (1 ≤ n ≤ 200) —
the number of points in the given set. Next n lines contain
the coordinates of the points written as "x y" (without the quotes)
(|x|, |y| ≤ 1000), all coordinates are integers.
The numbers in the line are separated by exactly one space.
It is guaranteed that all points are different.
===============================
Output
Print the only number — the number of supercentral points of the given set.
===============================
Sample test(s)

Input
8
1 1
4 2
3 1
1 2
0 2
0 1
1 0
1 3
Output
2

Input
5
0 0
0 1
1 0
0 -1
-1 0
Output
1
'''

##          Running Time  ===>>> 216 ms

N = int(input())

points =[None] * N
for i in range(N):
    points[i] = list(map(int, input().split()))

central_points = 0
for i in range(N):
    current_point = points[i]
    right, left, upper, lower = 0, 0, 0, 0
    for j in range(N):
        if i == j :
            continue
        elif current_point[1] == points[j][1]:
            if ( current_point[0] > points[j][0] and right == 0):
                right += 1
            elif (current_point[0] < points[j][0] and left == 0):
                left += 1

        elif current_point[0] == points[j][0]:
            if ( current_point[1] > points[j][1] and upper == 0):
                upper += 1
            elif (current_point[1] < points[j][1] and lower == 0):
                lower += 1
    if (right + left + upper + lower) == 4:
        central_points += 1

print(central_points)
        
