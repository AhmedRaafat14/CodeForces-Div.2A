'''
One day Dima and Alex had an argument about the price and quality of laptops.
Dima thinks that the more expensive a laptop is, the better it is.
Alex disagrees. Alex thinks that there are two laptops,
such that the price of the first laptop is less (strictly smaller)
than the price of the second laptop but the quality of the first laptop
is higher (strictly greater) than the quality of the second laptop.

Please, check the guess of Alex. You are given descriptions of n laptops.
Determine whether two described above laptops exist.
================================
Input
The first line contains an integer n (1 ≤ n ≤ 105) — the number of laptops.

Next n lines contain two integers each, ai and bi (1 ≤ ai, bi ≤ n),
where ai is the price of the i-th laptop,
and bi is the number that represents the quality of
the i-th laptop (the larger the number is, the higher is the quality).

All ai are distinct. All bi are distinct.
================================
Output
If Alex is correct, print "Happy Alex",
otherwise print "Poor Alex" (without the quotes).
================================
Sample test(s)

Input
2
1 2
2 1
Output
Happy Alex
'''

##              Running Time  ===>>>  529 ms

N = int(input())

laptops = [None] * N
for i in range(N):
    laptops[i] = list(map(int, input().split()))

if all(laptops[i][0] == laptops[i][1] for i in range(N)):
    print('Poor Alex')
else:
    laptops = sorted(laptops)
    
    if any(laptops[i][1] > laptops[i+1][1] for i in range(N-1)):
        print('Happy Alex')
    else:
        print('Poor Alex')


'''
##          Another Solution
##              Running Time  ===>>>  561 :: 670 ms

N = int(input())

laptops = [None] * N
for i in range(N):
    laptops[i] = list(map(int, input().split()))

laptops = sorted(laptops)

if any(laptops[i][1] > laptops[i+1][1] for i in range(N-1)):
    print('Happy Alex')
else:
    print('Poor Alex')
'''
