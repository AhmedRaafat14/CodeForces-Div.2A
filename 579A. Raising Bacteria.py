'''
problem told us every single bacteria split into two each day
so if we think for little bit we can find out 
when number of bacteria in box being odd this mean he puts 
a new one, so we count this one and we go throw till 
number user gives us it being zero or less we use in this 
integer division in python which give us integr value
 when we made it like this:
5 // 2 = 2
2 // 2 = 1
1 // 2 = 0
 bict    removed     answer
  5       1            1
  2       0            1
  1       1            2
  ======================
  7       1            1
  3       1            2
  1       1            3
'''

x = int ( input ( ) )

sol = 0

while x > 0: # 5, 2, 1, 0 then exit
    if x % 2 == 1:
        sol += 1 # 1, 2

    x //= 2 # 2, 1, 0

print(sol) # 2














#Another approche:
# by counting number of ones in binary reprsentation of number
print( bin(int(input())).count('1') )
