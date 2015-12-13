'''
Greg is a beginner bodybuilder. Today the gym coach gave him
the training plan. All it had was n integers a1, a2, ..., an.
These numbers mean that Greg needs to do exactly n exercises today.
Besides, Greg should repeat the i-th in order exercise ai times.

Greg now only does three types of exercises: "chest" exercises,
"biceps" exercises and "back" exercises. Besides, his training is
cyclic, that is, the first exercise he does is a "chest" one,
the second one is "biceps", the third one is "back",
the fourth one is "chest", the fifth one is "biceps",
and so on to the n-th exercise.

Now Greg wonders, which muscle will get the most exercise
during his training. We know that the exercise Greg repeats
the maximum number of times, trains the corresponding muscle the most.
Help Greg, determine which muscle will get the most training.
============================
Input
The first line contains integer n (1 ≤ n ≤ 20).
The second line contains n integers a1, a2, ..., 
an (1 ≤ ai ≤ 25) — the number of times Greg repeats the exercises.
============================
Output
Print word "chest" (without the quotes), if the chest gets the most exercise,
"biceps" (without the quotes), if the biceps gets the most exercise and print
"back" (without the quotes) if the back gets the most exercise.

It is guaranteed that the input is such that the answer to the problem is
unambiguous.
============================
Sample test(s)

Input
2
2 8
Output
biceps

Input
3
5 1 10
Output
back

Input
7
3 3 2 7 9 6 8
Output
chest
'''
##            Running Time ===>>>  186 ms
N = int(input())

exercises = list(map(int, input().split()))

chest = 0
biceps = 0
back = 0

trible_counter = 1
for i in range(N):
    if trible_counter > 3:
        trible_counter = 1

    if trible_counter == 1:
        chest += exercises[i]
        trible_counter += 1
        continue
    if trible_counter == 2:
        biceps += exercises[i]
        trible_counter += 1
        continue
    if trible_counter == 3:
        back += exercises[i]
        trible_counter += 1
        continue

if chest > biceps and chest > back:
    print('chest')
if biceps > chest and biceps > back:
    print('biceps')
if back > biceps and back > chest:
    print('back')


'''
##            Running Time ===>>>  248 ms

N = int(input())

exercises = list(map(int, input().split()))

answers = ['chest', 'biceps', 'back']
max_times = [0] * 3

trible_counter = 1
for i in range(N):
    if trible_counter > 3:
        trible_counter = 1

    if trible_counter == 1:
        max_times[0] += exercises[i]
        trible_counter += 1
        continue
    if trible_counter == 2:
        max_times[1] += exercises[i]
        trible_counter += 1
        continue
    if trible_counter == 3:
        max_times[2] += exercises[i]
        trible_counter += 1
        continue

print(answers[max_times.index(max(max_times))])
'''
