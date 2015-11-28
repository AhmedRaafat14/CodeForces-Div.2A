"""
Sometimes some words like "localization" or "internationalization"
are so long that writing them many times in one text is quite tiresome.
Let's consider a word too long, if its length is strictly more
than 10 characters. All too long words should be replaced
with a special abbreviation.

This abbreviation is made like this:
we write down the first and the last letter of a word and between them
we write the number of letters between the first and the last letters.
That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization»
will be spelt as "i18n".

You are suggested to automatize the process of changing the words with
abbreviations. At that all too long words should be replaced by
the abbreviation and the words that are not too long should not
undergo any changes.
===========
Input
The first line contains an integer n (1 ≤ n ≤ 100).
Each of the following n lines contains one word.
All the words consist of lowercase Latin letters and possess
the lengths of from 1 to 100 characters.
===========
Output
Print n lines. The i-th line should contain the result of replacing of
the i-th word from the input data.
===========
Sample test(s)

Input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
Output
word
l10n
i18n
p43s
"""

##              Running Time   ========>      	92 ms

##  Read N test cases (Number of words user will enter)
N = int(raw_input())

## Loop through this test cases
for unUsed in range(0, N):
    ## Read user word 
    user_word = raw_input()
    ## If user word is less than or equal 10 then its short
    if len(user_word) <= 10:
        print(user_word)
        continue
    ## Else if its greater than 10 so we should convert it in special
    ##   abbservation
    elif len(user_word) > 10:
        ## Get first char
        new_short_word = user_word[0]
        ## Get length without first and last chars
        long_word_size = len(user_word[0:-2])
        ## Construct new word by first and last chars between them its size
        new_short_word += str(long_word_size) + user_word[-1]
        ## Print new short word
        print(new_short_word)
