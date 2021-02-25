import random, string
from words import wordlist

# print(wordlist)

def get_vaild_word(wordlist):
    word = random.choice(wordlist) #randomly chooses something from the list

    while '-'in wordlist or' 'in word:
        word = random.choice(wordlist)
    
    return word.upper()

def hangman():
    word = get_vaild_word(wordlist)
    word_letters = set(word) #letters in the word

    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 10
    #getting user input

    while len(word_letters) > 0 and lives > 0: #len() : length
        #letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f'\nYou have {lives} live(s) left.\nYou have used these letters : ',' '.join(used_letters))

        #what current word is. (ie: W_RD)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else : 
                lives = lives - 1 #takes away a life if wrong
                print(f"Wrong! Try another letter.")
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else : 
            print('Invaild character.Please try again.')
    
    #gets here when len(word_letters) == 0 OR when lives ==0
    if lives == 0:
        print(f"\nToo bad. The word was this : {word}")
        input ('Press enter to close the window.')
    else:
        print(f"Wow! You guessed the word {word}!!\n")
        input ('\nPress enter to close the window.')
hangman()