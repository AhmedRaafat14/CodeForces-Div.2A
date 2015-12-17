'''
You've got a rectangular parallelepiped with integer edge lengths.
You know the areas of its three faces that have a common vertex.
Your task is to find the sum of lengths of all 12 edges of
this parallelepiped.
============================
Input
The first and the single line contains three space-separated integers
— the areas of the parallelepiped's faces.
The area's values are positive ( > 0) and do not exceed 104.
It is guaranteed that there exists at least one parallelepiped
that satisfies the problem statement.
============================
Output
Print a single number — the sum of all edges of the parallelepiped.
============================
Sample test(s)

Input
1 1 1
Output
12

Input
4 6 6
Output
28
'''

##              Running Time ===>>> 154 ms

import math
data = input().split()

A1, A2, A3 = int(data[0]), int(data[1]), int(data[2])

'''
    ##     A1 = LW   ===>>> so,  L = A1/W
    ##     A2 = LH   ===>>> so,  A2 = (A1/W)*H ==> A2 = (A1/(A3/H))*H
    ##                           A2 = (A1/A3) * H^2 ==> H^2 = (A2 * A3) / A1
    ##     A3 = WH   ===>>> so,  W = A3/H
'''
H   =   int(math.sqrt((A2 * A3) // A1))
W   =   A3 // H
L   =   A1 // W

## For rectangular parallelepiped cosists of 4 edges equal to L and
##     4 equal to W and 4 equal to H
print(4*L + 4*W + 4*H)
