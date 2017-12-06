# You can solve it in two approches

# Approche 1
# s = list(map(int, input().split())) # 1, 7, 3, 3
#
# sol = []
# for color in s: # 1, 7, 3, 3
#     if color not in sol: # 1, 7, 3, 3
#         sol.append(color) # 1, 7, 3
#
# print(4 - len(sol)) # sol = 1, 7, 3 ===> 1 -> res



# Approche 2
s = input().split()
#s = 7 7 7 7  => set(s) = set(7)
print( 4 - len(set(s)) ) # => 3

