n = int(input())

sol = 0
for i in range(n):
    p, q = list(map(int, input().split()))
    if (q - p) >= 2:
        sol += 1

print(sol)