#http://codeforces.com/contest/427/problem/A
'''
For this problem it's solution is so simple, just read
problem statement carefually and you will got the answer:

    Problem:
        In this problem we want count the number of untrated crimes

    Solution:
        To simple one just by iterate over the list and check if the
        current item is positive so this item is the number of hired
        police officers, then get the next item and check if it's
        negative so this is crime so check if we have police officers
        free in hired or not if we have so hire one of them to this
        crime and decrement it by one. Otherwise, we increment
        the untrated counter by one because we have a crime and doesn't
        have any free policeman.
        sudocode:
            Foreach el in range(li)
                if el > 0:
                    hired += el
                    go to next item
                if el < 0 and hired > 0:
                    hired -= 1
                    go to next item
                if el < 0 and hired < 1:
                    untrated += 1
                    go to next item
            print(untrated)


    Example:
        n  = 3
        li = -1 -1 1
        hired = untrated = 0

        O(N)

        Apply the prev sudocode descriped above:
        foreach el in li:
            el = -1 < 0 and hired < 1:
                untrated += 1 ===> untrated = 1
            el = -1 < 0 and hired < 1:
                untrated += 1 ===> untrated = 2
            el = 1 > 0:
                hired += el ==> hired = 1
            exit;

        print(untrated)  ==>>  2

'''
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
