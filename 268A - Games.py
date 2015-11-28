'''
Manao works on a sports TV. He's spent much time watching
the football games of some country. After a while he began
to notice different patterns. For example, each team has
two sets of uniforms: home uniform and guest uniform.
When a team plays a game at home, the players put on the home uniform.
When a team plays as a guest on somebody else's stadium,
the players put on the guest uniform. The only exception to that rule is:
when the home uniform color of the host team matches the guests' uniform,
the host team puts on its guest uniform as well. For each team
the color of the home and guest uniform is different.

There are n teams taking part in the national championship.
The championship consists of n·(n - 1) games: each team invites
each other team to its stadium. At this point Manao wondered:
how many times during the championship is a host team going to
put on the guest uniform? Note that the order of the games does
not affect this number.

You know the colors of the home and guest uniform for each team.
For simplicity, the colors are numbered by integers in such a way
that no two distinct colors have the same number. Help Manao find
the answer to his question.
=================================
Input
The first line contains an integer n (2 ≤ n ≤ 30).
Each of the following n lines contains a pair of distinct
space-separated integers hi, ai (1 ≤ hi, ai ≤ 100) —
the colors of the i-th team's home and guest uniforms, respectively.
=================================
Output
In a single line print the number of games where the host team is going
to play in the guest uniform.
=================================
Sample test(s)

Input
3
1 2
2 4
3 4
Output
1

Input
4
100 42
42 100
5 42
100 5
Output
5

Input
2
1 2
1 2

Output
0
=================================
Note
In the first test case the championship consists of 6 games.
The only game with the event in question is the game between teams 2 and 1
on the stadium of team 2.

In the second test sample the host team will have to wear guest uniform in
the games between teams: 1 and 2, 2 and 1, 2 and 3, 3 and 4, 4 and 2
(the host team is written first).
'''
##                  Running Time   ====>>   124 ms

N = int(input())

teams_colors = [[0]*2] *N
for i in range(N):
    teams_colors[i] = input().split()

host_player = []
guest_player = []

number_of_games = 0
'''
Ex.
user Input:
        3
        1 2
        2 4
        3 4
Solution:
         Team #       Home Color       Guest Color
         1                1                 2
         2                2                 4
         3                3                 4
    Number of games is :   N*(N-1)  = 3*(3-1) = 6
    this code doesn't loop through tehm in one loop but its two loop
    and the second loop ignore the index which equal the index in 'i' === n-1

    So, its loop for each Team and check if in this game if this host team
    home color equal to the guest color... increment the counter whiche refer
    to the # of games whiche any host team puts its guest color:

    For team #1 ==> i == 0:
    team1 playes team2 :  team1 put home color and team2 put its guest color
      1            4
      cuz team1 home color not equal to team2 guest color ignore the condition
    team1 playes team3 :  team1 put home color and team3 put its guest color
      1            4
    For team #2 ==> i == 1:
    team2 playes team1 :  team2 put guest color and team1 put its guest color
      4            2
      cuz team2 home color equal to team1 guest color so team2 must put guest
      color and increment counter by 1
    and so on until the end
'''
for i in range(N):
    host_player = teams_colors[i]
    for j in range(N):
        if j != i:
            guest_player = teams_colors[j]
            if host_player[0] == guest_player[1]:
                number_of_games += 1

print(number_of_games)
