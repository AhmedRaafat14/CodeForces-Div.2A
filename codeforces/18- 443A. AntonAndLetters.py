'''
Recently, Anton has found a set. The set consists of small English letters.
Anton carefully wrote out all the letters from the set in one line,
separated by a comma. He also added an opening curved bracket at the
beginning of the line and a closing curved bracket at the end of the line.

Unfortunately, from time to time Anton would forget writing some letter
and write it again. He asks you to count the total number of distinct
letters in his set.
================================
Input
The first and the single line contains the set of letters.
The length of the line doesn't exceed 1000.
It is guaranteed that the line starts from an opening curved bracket and
ends with a closing curved bracket. Between them,
small English letters are listed, separated by a comma.
Each comma is followed by a space.
================================
Output
Print a single number — the number of distinct letters in Anton's set.
================================
Sample test(s)

Input
{a, b, c}
Output
3

Input
{b, a, b, a}
Output
2

Input
{}
Output
0
'''
##              Running TimeoutError    ====>>>   77 ms

anton_letters = input()

if len(anton_letters[1:-1]) > 0:
    anton_letters = anton_letters[1:-1].replace(' ', '')
    print(len(set(anton_letters.split(','))))
else:
    print('0')
