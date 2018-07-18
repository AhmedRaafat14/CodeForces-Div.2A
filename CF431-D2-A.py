calories = list(map(int, input().split()))

game = input()


# First approach
ans = game.count('1') * calories[0] + game.count('2') * calories[1] \
      + game.count('3') * calories[2] + game.count('4') * calories[3]

# Second approach
# ans = 0
# for sq in game:
#     ans += calories[int(sq) - 1]

print(ans)
