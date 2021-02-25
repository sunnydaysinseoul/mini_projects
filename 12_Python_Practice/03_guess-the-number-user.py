import random
# 'random'is python standard library. https://docs.python.org/3/library/random.html

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != "c":
        if low !=high:
            guess = random.randint(low,high)
        else:
            guess = low #it could also be high  b/c low = high

        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        # ".lowercase" was not working so I used "".lower()""
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Hooray! The computer guessed your number, {guess}, correctly!")

computer_guess(30); #여기서 최대값을 정해주고 그 안에서 내가 원하는 값을 생각하기
input ('\nPress enter to close the window.')

