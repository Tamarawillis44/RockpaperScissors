
import random
#  random.choice(sequence) ..equired. A sequence like a list, a tuple, a range of numbers etc
def play():
    user = input("Whats youre choice? 'r' for rock, 'p' for paper, 's' for scissors:  ")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'It\'s a tie. MY choice, {computer}'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return f'You won!, MY choice, {computer}'

    return f'You lost. MY choice, {computer}'

def is_win(player, opponent):
    # return true if player wins
# r > s, S > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
