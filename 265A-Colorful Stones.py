# http://codeforces.com/contest/265/problem/A

S = input()  # R R R B G B R B B B
T = input()  # B B B R R

liss_pos = 0
for i in range( len(T) ):
    if T[i] == S[liss_pos]: # i = 4, pos = 0, R == R
        liss_pos += 1  # pos += 1 ==> 2

print(liss_pos + 1) # 3 in 1-bassed
