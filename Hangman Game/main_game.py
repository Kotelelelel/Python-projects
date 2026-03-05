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
word_matrix = []
guesses = []

for i in word:
    word_matrix.append(i)

while lives > 0:
    print(f"You have {lives} more tries")
    print("Write your guess: ")
    guess = input()

    if guess in guesses:
        print("You already guessed this letter")
        printer(word,guesses)
    else:
        if guess in word:
            guesses.append(guess)
            if set(word_matrix).issubset(guesses):
                print("You won!")
                print(f"The word is {word}")
                break
            else:
                printer(word,guesses)
                continue
        else:
            guesses.append(guess)
            lives-=1
            if lives > 0 :
                print('Wrong')
                printer(word,guesses)
            else:
                print("You lost!")
                print(f"The word was {word}")
            
