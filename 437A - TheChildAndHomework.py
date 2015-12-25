'''
Once upon a time a child got a test consisting of multiple-choice
questions as homework. A multiple-choice question consists of four choices:
A, B, C and D. Each choice has a description, and the child should find out
the only one that is correct.

Fortunately the child knows how to solve such complicated test.
The child will follow the algorithm:

    -- If there is some choice whose description at least twice shorter
          than all other descriptions, or at least twice longer than
          all other descriptions, then the child thinks the choice is great.
    -- If there is exactly one great choice then the child chooses it.
          Otherwise the child chooses C (the child think it is
          the luckiest choice). 

You are given a multiple-choice questions, can you predict child's choose?
=============================
Input
The first line starts with "A." (without quotes),
then followed the description of choice A.
The next three lines contains the descriptions of
the other choices in the same format. They are given in order: B, C, D.
Please note, that the description goes after prefix "X.",
so the prefix mustn't be counted in description's length.

Each description is non-empty and consists of at most 100 characters.
Each character can be either uppercase English letter or
lowercase English letter, or "_".
=============================
Output
Print a single line with the child's choice:
"A", "B", "C" or "D" (without quotes).
=============================
Sample test(s)

Input
A.VFleaKing_is_the_author_of_this_problem
B.Picks_is_the_author_of_this_problem
C.Picking_is_the_author_of_this_problem
D.Ftiasch_is_cute
Output
D

Input
A.ab
B.abcde
C.ab
D.abc
Output
C

Input
A.c
B.cc
C.c
D.c
Output
B
'''

##              Running Time   ===>>>   61 ms

A = len(input()[2:])
B = len(input()[2:])
C = len(input()[2:])
D = len(input()[2:])

answer = 'C'
counter = 0

if ( all(A >= e*2 for e in [B, C, D]) or
     all(A <= (e//2) for e in [B, C, D]) ):
    answer = 'A'
    counter += 1
if ( all(B >= e*2 for e in [A, C, D]) or
     all(B <= (e//2) for e in [A, C, D]) ):
    answer = 'B'
    counter += 1
if ( all(C >= e*2 for e in [A, B, D]) or
     all(C <= (e//2) for e in [A, B, D]) ):
    answer = 'C'
    counter += 1
if ( all(D >= e*2 for e in [A, B, C]) or
     all(D <= (e//2) for e in [A, B, C]) ):
    answer = 'D'
    counter += 1

if counter == 1:
    print(answer)
else:
    print('C')
