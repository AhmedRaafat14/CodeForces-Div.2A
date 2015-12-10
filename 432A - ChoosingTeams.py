'''
The Saratov State University Olympiad Programmers Training Center
(SSU OPTC) has n students. For each student you know the number of
times he/she has participated in the ACM ICPC world programming championship.
According to the ACM ICPC rules, each person can participate in
the world championship at most 5 times.

The head of the SSU OPTC is recently gathering teams to participate in
the world championship. Each team must consist of exactly three people,
at that, any person cannot be a member of two or more teams.
What maximum number of teams can the head make if he wants each team to
participate in the world championship with the same members at least k times?
=======================================
Input
The first line contains two integers, n and k (1 ≤ n ≤ 2000; 1 ≤ k ≤ 5).
The next line contains n integers: y1, y2, ..., yn (0 ≤ yi ≤ 5), where yi
shows the number of times the i-th person participated in the ACM ICPC world
championship.
=======================================
Output
Print a single number — the answer to the problem.
=======================================
Sample test(s)

Input
5 2
0 4 5 1 0
Output
1

Input
6 4
0 1 2 3 4 5
Output
0

Input
6 5
0 0 0 0 0 0
Output
2
'''

##   First Solution           Running Time =====>>>> 62 ms

data = input().split()
std_times = input().split()

N, K = int(data[0]), int(data[1])
std_times = sorted(list(map(int, std_times)))

'''
      #  Count all students which there times + K less than o equal
      #  to 5, and then divide this number by 3 to get # of teams
'''
teams = 0
i = 0
while i < N :
    if std_times[i] + K <= 5:
        teams += 1
    i += 1

print(teams//3)


'''
##   Second Solution           Running Time =====>>>> 62 ms

data = input().split()
std_times = input().split()

N, K = int(data[0]), int(data[1])
std_times = list(map(int, std_times))

# if all of them is equal to 0 so print # of them divide by 3
if all(e == 0 for e in std_times):
    print(N//3)
    exit
else:
    # otherwise sort them first
    std_times = sorted(std_times)
    
    teams = 0
    i = 0
    # just loop through number of them divided by 3
    # and check for each connected trible students there's 3 of times + K
    #  less than 5
    while N//3 :
        if i == N-1 or i >= N:
            break
        elif (std_times[i]+K) <= 5 and (std_times[i+1]+K) <= 5 and (std_times[i+2]+K) <= 5:
            teams += 1
            i += 3
            continue
        else:
            i += 1

    print(teams)
'''
