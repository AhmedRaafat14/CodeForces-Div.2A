from typing import List

n = int(input())
friends = list(map(int, input().split()))

sol = [0] * n

for i in range(n):
    sol[friends[i] - 1]  = i + 1

print(" ".join(map(str, sol)))
