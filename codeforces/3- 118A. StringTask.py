"""
Petya started to attend programming lessons.
On the first lesson his task was to write a simple program.
The program was supposed to do the following: in the given string,
consisting if uppercase and lowercase Latin letters, it:

    1. deletes all the vowels,
    2. inserts a character "." before each consonant
    3. replaces all uppercase consonants with corresponding lowercase ones. 

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants.
The program's input is exactly one string, it should return the output as a
single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.
==============
Input
The first line represents input string of Petya's program.
This string only consists of uppercase and lowercase Latin letters and
its length is from 1 to 100, inclusive.
==============
Output
Print the resulting string. It is guaranteed that this string is not empty.
==============
Sample test(s)

Input
tour
Output
.t.r

Input
Codeforces
Output
.c.d.f.r.c.s

Input
aBAcAba
Output
.b.c.b
"""

##              Running Time   ========>      	122 ms

## input string of Petya's program
user_word = raw_input()
## convert it to lower case string
##   3. replaces all uppercase consonants with corresponding lowercase ones.
user_word = user_word.lower()
## define vowels string
vowels = 'aoyeui'
## define new word
new_word = ''
## loop through user string and check if character not in vowels string
##      add it to new word string and add before it '.'
##    1. deletes all the vowels,
##    2. inserts a character "." before each consonant,
for char in user_word:
    if char not in vowels:
        new_word += '.' + char

## print new word
print(new_word)
