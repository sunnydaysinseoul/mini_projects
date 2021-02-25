import random

def play():
    user = input("What's your choice?\n'r' for rock, 's' for scissors, 'p' for paper : \n").lower()
    computer = random.choice(['r','s','p'])

    if user == computer:
        return "Oh! It's a tie."

    # r>s, s>p, p>r
    if is_win(user, computer):
        return "You won!"
    else :
        return "You lost... Try again?"


def is_win(player, opponent):
    #return true if player wins
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True

print(play())
input ('\nPress enter to close the window.')