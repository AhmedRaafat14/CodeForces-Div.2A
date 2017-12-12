#http://codeforces.com/contest/567/problem/A

n = int(input())
cits = list(map(int, input().split()))

sol = []

for i in range(n):
    mx = max(abs(cits[i] - cits[0]), abs(cits[i] - cits[-1]))
    if i == 0:
        mn = abs(cits[i] - cits[i + 1])
    elif i == n - 1:
        mn = abs(cits[i] - cits[ i - 1])
    else:
        mn = min(abs(cits[i] - cits[i - 1]), abs(cits[i] - cits[i + 1]))
    sol.append([mn, mx])

for row in sol:
    print(*row)
