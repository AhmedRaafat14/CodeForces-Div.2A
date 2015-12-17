'''
Vasya, or Mr. Vasily Petrov is a dean of a department in a local
university. After the winter exams he got his hands on a group's gradebook.

Overall the group has n students. They received marks for m subjects.
Each student got a mark from 1 to 9 (inclusive) for each subject.

Let's consider a student the best at some subject, if there is no student
who got a higher mark for this subject. Let's consider a student successful,
if there exists a subject he is the best at.

Your task is to find the number of successful students in the group.
===============================
Input
The first input line contains two integers n and m (1 ≤ n, m ≤ 100) —
the number of students and the number of subjects, correspondingly.
Next n lines each containing m characters describe the gradebook.
Each character in the gradebook is a number from 1 to 9.
Note that the marks in a rows are not sepatated by spaces.
===============================
Output
Print the single number — the number of successful students in
the given group.
===============================
Sample test(s)

Input
3 3
223
232
112
Output
2

Input
3 5
91728
11828
11111
Output
3
'''

##      Running Time   ===>>>  826 ms

data = input().split()

N, M = int(data[0]), int(data[1])

marks = [None] * N
for i in range(N):
    marks[i] = input()

answer = 0
subj = []
if N == 1:
    print(N)
else:
    for i in range(N):
        tmp_answer = 0
        for col in range(M):
            flag = 1
            for j in range(N):
                if int(marks[j][col]) > int(marks[i][col]):
                    flag = 0
            if flag == 1:
                tmp_answer = 1
        if tmp_answer == 1:
            answer += 1

    print(answer)
