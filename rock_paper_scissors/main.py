import random

def play():
  user = input("'r' for rock, 'p' for paper and 's' for scissors: ")
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return 'tie'

  if is_win(user, computer):
    return 'You won!'

  return 'You lost!'

def is_win(player, oponent):
    # r > s, s > p, p > r
  if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'p' and oponent == 'r'):
    return True

print (play())