import random
# 'random'is python standard library. https://docs.python.org/3/library/random.html


# define a function
def guess(x):
    random_number = random.randint(1,x)
    # random.randint(a, b) means
    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} : "));
        # 여기에 int안써서 오류났었음! str으로 인식해서 random_number(int)와 비교불가
        
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Hooray! You've got it right! The answer was {random_number}.")

guess(17);
input ('\nPress enter to close the window.')

