'''
Devu is a renowned classical singer. He is invited to many big
functions/festivals. Recently he was invited to
"All World Classical Singing Festival".
Other than Devu, comedian Churu was also invited.

Devu has provided organizers a list of the songs and
required time for singing them. He will sing n songs,
ith song will take ti minutes exactly.

The Comedian, Churu will crack jokes. All his jokes are of 5 minutes exactly.

People have mainly come to listen Devu. But you know that he
needs rest of 10 minutes after each song. On the other hand,
Churu being a very active person, doesn't need any rest.

You as one of the organizers should make an optimal sсhedule for the event.
For some reasons you must follow the conditions:

    - The duration of the event must be no more than d minutes;
    - Devu must complete all his songs;
    - With satisfying the two previous conditions the number of
         jokes cracked by Churu should be as many as possible. 

If it is not possible to find a way to conduct all the songs of the Devu,
output -1. Otherwise find out maximum number of jokes
that Churu can crack in the grand event.
============================
Input
The first line contains two space separated integers n, d
(1 ≤ n ≤ 100; 1 ≤ d ≤ 10000). The second line contains
n space-separated integers: t1, t2, ..., tn (1 ≤ ti ≤ 100).
============================
Output
If there is no way to conduct all the songs of Devu, output -1.
Otherwise output the maximum number of jokes that Churu can crack in
the grand event.
============================
Sample test(s)

Input
3 30
2 2 1
Output
5

Input
3 20
2 1 1
Output
-1
'''

##          Running Time  ===>>> 62 ms

data = input().split()

N, D = int(data[0]), int(data[1])

songs_t = input().split()
songs_t = list(map(int, songs_t))

rest_t = []
jocks_count = 0
'''
    count all songs till N-1 for each song sum its time on the rest time 10 Min
    so it will like this t1 * 10 + t2 * 10 +.....+ t(n-1) * 10
    and for each song there will be at most 2 jocks cracked by churu so count
    them and after this add last song without any rest cuz its the end
    and then check if sum(new songs times) > all event time so there's
    no way to Devu to sing his all songs so prnt '-1'
    otherwis print the number of jocks counted add to the rest fo time after last
    song by this eq:
         D - sum(new songs times) // 5 [integer division]
    and 5 is the time for jocks
'''
for i in range(0, N-1):
    rest_t.append(songs_t[i] + 10)
    jocks_count += 2

rest_t.append(songs_t[-1])

if sum(rest_t) > D:
    print('-1')
else:
    print(jocks_count + (D - sum(rest_t))//5)
