# http://codeforces.com/contest/266/problem/A

'''
For this problem it's solution is so simple, just understand
problem statement and you will got the answer:

    Problem:
        In this problem we want count min number of stones we should
        take it from table to make all stones no two neighboring
        stones will have same color.

    Solution:
        To simple just we want count number of neighboring stones
        which have same color and want to take one of them to take it.

    Example:
        n  = 3
        st = R R G
        ans = 0

        Foreach i in range(n - 1)
        ((  because we can't count last stone
                with any neighboring one after it. ))
        check if current stone color == to next one so count it
        from i = 0 to i = n - 1 = 2
        i = 0:
            st[i] == st[i + 1] ==>  st[0] == st[1] ==> 'R' == 'R'
                YES so ans += 1
                ans = 1
        i = 1:
            st[i] == st[i + 1] ==>  st[2] == st[2] ==> 'R' == 'G'
                NO so ans stay as it
                ans = 1
        i == 2 == n - 1 so break the loop

        then print(  ans  ) ==>  1
'''

N = int ( input ( ) )  # 5

colors = input ( )  # R R R R R

sol = 0

for i in range ( N - 1 ):  # i = 0 to i = 4
    if colors[ i ] == colors[ i + 1 ]:
        sol += 1

print(sol)
