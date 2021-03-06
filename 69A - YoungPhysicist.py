'''
A guy named Vasya attends the final grade of a high school.
One day Vasya decided to watch a match of his favorite hockey team.
And, as the boy loves hockey very much, even more than physics,
he forgot to do the homework. Specifically,
he forgot to complete his physics tasks.
Next day the teacher got very angry at Vasya and decided to teach him a lesson.
He gave the lazy student a seemingly easy task: You are given an idle body in
space and the forces that affect it. The body can be considered as a material
point with coordinates (0; 0; 0). Vasya had only to answer whether it is in
equilibrium. "Piece of cake" — thought Vasya, we need only to check if
the sum of all vectors is equal to 0. So, Vasya began to solve the problem.
But later it turned out that there can be lots and lots of these forces,
and Vasya can not cope without your help. Help him.
Write a program that determines whether a body is idle or is moving by
the given vectors of forces.
======================================
Input
The first line contains a positive integer n (1 ≤ n ≤ 100),
then follow n lines containing three integers each: the xi coordinate,
the yi coordinate and the zi coordinate of the force vector, applied to
the body ( - 100 ≤ xi, yi, zi ≤ 100).
======================================
Output
Print the word "YES" if the body is in equilibrium, or the word "NO" if
it is not.
======================================
Sample test(s)

Input
3
4 1 7
-2 4 -1
1 -5 -3
Output
NO

Input
3
3 -1 7
-5 2 -4
2 -1 -3
Output
YES
'''

##                  Running Time   ====>>>   154 ms

import math

# Read number of forces used on body
N = int(input())
## Define the matrix which hold the N-th forces vectors
XYZ_axis = [[0]*3] * N
for i in range(N):
    tmp = input().split()
    XYZ_axis[i] = list(map(int, tmp))

##  Calculate the sum of powerd forces to 2 and take its sqrt to check
##    if its == 0 so the body is equilibrium and print YES
##    otherwise print NO

##    The rule used is:
##          g force = sqrt(X^2 + Y^2 + Z^2)
axis_sum = 0
for j in range(3):
    sum_tmp = 0
    for i in range(N):
        sum_tmp += XYZ_axis[i][j]
    sum_tmp **= 2
    axis_sum += sum_tmp

if math.sqrt(axis_sum) == 0.0:
    print("YES")
else:
    print("NO")

'''
##		Another Solutuin
##		Running Time =====>>>>    124 ms

## Just check if sum(Xi) and sum(Yi) and Sum(Zi) all of them equal to zero

N = int(input())

XYZ_axis = [[0]*3] * N
for i in range(N):
    tmp = input().split()
    XYZ_axis[i] = list(map(int, tmp))

axis_sum = []
for j in range(3):
    sum_tmp = 0
    for i in range(N):
        sum_tmp += XYZ_axis[i][j]
    
    axis_sum.append(sum_tmp)

if all(e == 0 for e in axis_sum):
    print("YES")
else:
    print("NO")

'''
