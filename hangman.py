
# hangman game

import random

words = ['dead', 'laptop', 'america']
word = random.choice(words)

won = 0
name = input('Enter your name ')
print('Hello ', name, ' How are you doing today.\nLets play a word guess game.')
print('Guess This ', len(word), ' letter word \nYou have To guess this word by guessing letters.\nYou have 10 healths, One health will be reduced for each wrong answer')

valid = set('abcdefghijklmnopqrstuvwxyz')

guessed = []
hangman = 'HANGTODEAD'
attempts = 10



def start():
    global attempts, won
    if len(guessed) == len(word):
        print('')
        print('YOU WON')
    elif attempts == 0:
        pass
    elif won == 1:
        print('You Won')

    else:
        createword()
        if won == 0:
            getletter()
        start()

def createword():
    global won
    x = 0
    for i in word:
        if i in guessed:
            print(i, end=" ")
        else:
            x = 1
            print("_", end=" ")
    if x == 0:
        won = 1


def getletter():
    global word
    global attempts
    if attempts != 0:
        letter = input('enter letter ')
        if letter.isalpha() and len(letter)>=1:
            if letter in word:
                print('Well Guessed')
                word = random.choice(words)
                guessed.append(letter)

            else:
                print('wrong letter')
                attempts = attempts - 1
                print('')
                print('attempts remaining', attempts)
                for j in range(0, (10 - attempts)):
                    print(hangman[j], end='')

                print()
                if attempts == 0:

                    print('You LOSE')
                    print('GAME OVER')

        else:
            print('enter valid letter in small alphabets')


start()

