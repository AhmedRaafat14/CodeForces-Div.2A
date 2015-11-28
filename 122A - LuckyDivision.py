"""
Petya loves lucky numbers. Everybody knows that lucky numbers are
positive integers whose decimal representation contains only the lucky
digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467
are not.

Petya calls a number almost lucky if it could be evenly divided by some
lucky number. Help him find out if the given number n is almost lucky.
=====================
Input
The single line contains an integer n (1 ≤ n ≤ 1000) —
the number that needs to be checked.
=====================
Output
In the only line print "YES" (without the quotes),
if number n is almost lucky. Otherwise, print "NO" (without the quotes).
=====================
Sample test(s)

Input
47
Output
YES

Input
16
Output
YES

Input
78
Output
NO
=====================
Note
Note that all lucky numbers are almost lucky as any number is evenly
divisible by itself.

In the first sample 47 is a lucky number.
In the second sample 16 is divisible by 4.
"""

##                      Running Time   =====>>     122 ms

N = raw_input()

lucky = 0
lucky_numbers = { 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777}

if any(int(N)%c == 0 for c in lucky_numbers):
    print("YES")
else:
    print("NO")

"""
##			Another Solution ====>>> 124 ms

N = raw_input()


if all(c == '4' for c in N):
    print("YES")
    exit
elif all(c == '7' for c in N):
    print("YES")
    exit
elif all(c == '7' or c == '4'  for c in N):
    print("YES")
    exit
else:
    lucky = 0
    tmp = 4
    while True:
        if all(c == '4' for c in str(tmp)) and tmp <= 744:
            if int(N)%tmp == 0 or int(N)%(tmp+3) == 0:
                lucky = 1
                break
        else:
            break
        tmp += 40

    if lucky == 1:
        print("YES")
    else:
        print("NO")
"""

"""
##			Another Solution ====>>> 122 ms

N = raw_input()

##   Casse #1: if all number is '4' so its lucky
if all(c == '4' for c in N):
    print("YES")
    exit
##   Casse #2: if all number is '7' so its lucky
elif all(c == '7' for c in N):
    print("YES")
    exit
##   Casse #3: if all number is '4' and '7' only so its lucky
elif all(c == '7' or c == '4'  for c in N):
    print("YES")
    exit
##   Casse #4: if its not contain '4' or '7' so check if it divisable by
##          lucky one
else:
    lucky = 0
    lucky_numbers = { 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777}
    while True:
        if any(int(N)%c == 0 for c in lucky_numbers):
            lucky = 1
            break
        else:
            break

    if lucky == 1:
        print("YES")
    else:
        print("NO")
"""
