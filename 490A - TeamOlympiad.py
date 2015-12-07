'''
The School №0 of the capital of Berland has n children studying in it.
All the children in this school are gifted:
some of them are good at programming, some are good at maths,
others are good at PE (Physical Education). Hence,
for each child we know value ti:

    ti = 1, if the i-th child is good at programming,
    ti = 2, if the i-th child is good at maths,
    ti = 3, if the i-th child is good at PE 

Each child happens to be good at exactly one of these three subjects.

The Team Scientific Decathlon Olympias requires teams of three students.
The school teachers decided that the teams will be composed of
three children that are good at different subjects. That is,
each team must have one mathematician, one programmer and one sportsman.
Of course, each child can be a member of no more than one team.

What is the maximum number of teams that the school
will be able to present at the Olympiad?
How should the teams be formed for that?
================================
Input
The first line contains integer n (1 ≤ n ≤ 5000) —
the number of children in the school.
The second line contains n integers t1, t2, ..., tn
(1 ≤ ti ≤ 3), where ti describes the skill of the i-th child.
================================
Output
In the first line output integer w — the largest possible number of teams.

Then print w lines, containing three numbers in each line.
Each triple represents the indexes of the children forming the team.
You can print both the teams, and the numbers in the triplets in any order.
The children are numbered from 1 to n in the order of their appearance in
the input. Each child must participate in no more than one team.
If there are several solutions, print any of them.

If no teams can be compiled, print the only line with value w equal to 0.
================================
Sample test(s)

Input
7
1 3 1 3 2 1 2
Output
2
3 5 2
6 7 4

Input
4
2 1 1 2
Output
0
'''

'''
##  This solution depends on seperate the all 1s, 2s and 3s each one of them
##     in a one array and then take each column of each array and count teams
##      when counter be greater than one of 3 arrays so break and print data

##              Running Time  ===>>>  77 ms   [O(N)]

N = int(input())

t_data = input().split()

if t_data.count('1') == 0 or t_data.count('2') == 0 or t_data.count('3') == 0:
    print('0')
    exit
else:
    t1 = [(i+1, t_data[i]) for i in range(N) if t_data[i] == '1']
    t2 = [(i+1, t_data[i]) for i in range(N) if t_data[i] == '2']
    t3 = [(i+1, t_data[i]) for i in range(N) if t_data[i] == '3']

    teams = []
    team_counter = 0
    while True:
        if len(t1)-1 < team_counter or len(t2)-1 < team_counter or len(t3)-1 < team_counter:
            break
        teams.append([t1[team_counter][0], t2[team_counter][0], t3[team_counter][0]])
        team_counter += 1

    print(team_counter)
    print("\n".join(" ".join(map(str, line)) for line in teams))

'''
##  This solution depends on loop through one array and get 3 members
##     at one time and put its data to empty to never take them again
##      and count team too when counter be equal to N or N-1 or there's no 
##      any one of 1s, 2s or 3s in array break and print data
##  this solution takes more time cuz it loops through the each element in array

##          Running Time ====>>>   685 ms     [O(N^2)]

N = int(input())

t_data = input().split()

if t_data.count('1') == 0 or t_data.count('2') == 0 or t_data.count('3') == 0:
    print('0')
    exit
else:
    t_cpy = t_data.copy()
    teams = []
    teams_count = 0
    counter = 0
    
    while True:
        if counter == N-1 or counter == N or t_cpy.count('1') == 0 or t_cpy.count('2') == 0 or t_cpy.count('3') == 0:
            break
        t1 = t_cpy.index('1')
        t2 = t_cpy.index('2')
        t3 = t_cpy.index('3')
        
        t_cpy[t1] = ''
        t_cpy[t2] = ''
        t_cpy[t3] = ''
        teams.append([(t1+1), (t2+1), (t3+1)])
        counter += 3
        teams_count += 1

    print(teams_count)
    print("\n".join(" ".join(map(str, line)) for line in teams))
