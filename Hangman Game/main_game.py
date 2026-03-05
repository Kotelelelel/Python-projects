import random

def printer(word,guesses):
    for character in word:
        if character in guesses:
            print(character)
        else:
            print('*')

lives = 7
words = ['banana','python','rabbit','phone','keyboard','panda','terminal']
word = random.choice(words)
guesses = []

while lives > 0:
    print(f"You have {lives} more tries")
    printer(word,guesses)
    print("Write your guess: ")
    guess = input().lower()

    if guess in guesses:
        print("You already guessed this letter")
    else:
        if guess in word:
            guesses.append(guess)
            if all(letter in guesses for letter in word):
                print("You won!")
                print(f"The word is {word}")
                break
        else:
            guesses.append(guess)
            lives-=1
            if lives > 0 :
                print('Wrong')
            else:
                print("You lost!")
                print(f"The word was {word}")
            
