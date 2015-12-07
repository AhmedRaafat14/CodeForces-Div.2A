'''
Today Patrick waits for a visit from his friend Spongebob.
To prepare for the visit, Patrick needs to buy some goodies in two
stores located near his house. There is a d1 meter long road between
his house and the first shop and a d2 meter long road between his house
and the second shop. Also, there is a road of length d3 directly
connecting these two shops to each other. Help Patrick calculate
the minimum distance that he needs to walk in order to go to both shops
and return to his house.

Patrick always starts at his house. He should visit both shops moving
only along the three existing roads and return back to his house.
He doesn't mind visiting the same shop or passing the same road multiple times. The only goal is to minimize the total distance traveled.
=========================
Input
The first line of the input contains three integers d1, d2, d3
(1 ≤ d1, d2, d3 ≤ 108) — the lengths of the paths.

    d1 is the length of the path connecting Patrick's house and the first shop;
    d2 is the length of the path connecting Patrick's house and the second shop;
    d3 is the length of the path connecting both shops. 
=========================
Output
Print the minimum distance that Patrick will have to walk in order to
visit both shops and return to his house.
=========================
Sample test(s)

Input
10 20 30
Output
60

Input
1 1 5
Output
4
'''
##                  Running Time  ====>>>   62 ms

data = input().split()

d1, d2, d3   =   int(data[0]), int(data[1]), int(data[2])

'''
The principle of the possibilities:(select min one of them)
         1- house --> first shop --> house --> second shop --> house
                  d1             d1        d2              d2
         2- house --> first shop --> second shop --> house
                  d1             d3              d2
         3- house --> first shop --> second shop --> first shop --> house
                  d1             d3              d3             d1
         4- house --> second shop --> first shop --> second shop --> house
                  d2              d3             d3              d2
'''

print(min(d1+d1+d2+d2, d1+d3+d2, d1+d3+d3+d1, d2+d3+d3+d2))
