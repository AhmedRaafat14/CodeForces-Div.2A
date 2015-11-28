'''
The end of the school year is near and Ms. Manana,
the teacher, will soon have to say goodbye to a yet another class.
She decided to prepare a goodbye present for her n students and give
each of them a jigsaw puzzle (which, as wikipedia states, is a tiling puzzle
that requires the assembly of numerous small, often oddly shaped, interlocking
and tessellating pieces).

The shop assistant told the teacher that there are m puzzles in the shop,
but they might differ in difficulty and size. Specifically, the first jigsaw
puzzle consists of f1 pieces, the second one consists of f2 pieces and so on.

Ms. Manana doesn't want to upset the children, so she decided that
the difference between the numbers of pieces in her presents
must be as small as possible. Let A be the number of pieces in
the largest puzzle that the teacher buys and B be the number of pieces in
the smallest such puzzle. She wants to choose such n puzzles that A - B is
minimum possible. Help the teacher and find the least possible value of A - B.
================================
Input
The first line contains space-separated integers n and m (2 ≤ n ≤ m ≤ 50).
The second line contains m space-separated integers f1, f2, ..., fm
(4 ≤ fi ≤ 1000) — the quantities of pieces in the puzzles sold in the shop.
================================
Output
Print a single integer — the least possible difference the teacher can obtain.
================================
Sample test(s)

Input
4 6
10 12 10 7 5 22
Output
5
================================
Note
Sample 1. The class has 4 students. The shop sells 6 puzzles.
If Ms. Manana buys the first four puzzles consisting of 10, 12, 10 and 7
pieces correspondingly, then the difference between the sizes of the largest
and the smallest puzzle will be equal to 5. It is impossible to obtain a
smaller difference. Note that the teacher can also buy puzzles 1, 3, 4 and 5
to obtain the difference 5.
'''

##              Running Time  ==>>  124 ms

N_M = input().split()

N, M =  int(N_M[0]), int(N_M[1])

puzzles = input().split()
puzzles = list(map(int, puzzles))

difference_counter = []
##      Sort the buzzles
puzzles = sorted(puzzles)
## Loop through it in number of students and get each set of puzzless' minimum
##      Value
for P_idx in range(M):
    stu_counter = 0
    students_tmp = []
    S_idx = P_idx
    while True:
        if stu_counter == N:
            break
        if S_idx == M-1:
            students_tmp.append(puzzles[S_idx])
            S_idx = 0
            stu_counter += 1
            continue
        students_tmp.append(puzzles[S_idx])
        S_idx += 1
        stu_counter += 1
    
    difference_counter.append(max(students_tmp) - min(students_tmp))
    

print(min(difference_counter))
