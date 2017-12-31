#http://codeforces.com/contest/427/problem/A

n = int(input())

li = list(map(int, input().split()))

hired = untrated = 0

for el in li:
    if el == abs(el):
        hired += el
        continue
    if hired > 0 and el != abs(el):
        hired -= 1
        continue
    if hired == 0 and el != abs(el):
        untrated += 1

print(untrated)
