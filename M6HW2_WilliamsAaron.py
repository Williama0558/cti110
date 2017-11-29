#CTI-110
#M6HW2 - Guessing Game
#Aaron Williams
#11/29/17
#This program generates a random number that the user has to guess.

import random

def main():
    print('Welcome to the Random Number Guesser')
    print('')
    playGame()
    userChoice = input('Do you want to play again? y/n: ')
    #Replays the game if the user enters in 'y'
    if userChoice == 'y':
        main()
    else:
        print('Thanks for playing!')


def playGame():
    userGuess = True
    #Generates the random number
    number = random.randint(0,100)
    guesses = 0
    #Runs the loop until the user guesses the right number
    while userGuess != number:
        userGuess = int(input('Please guess a random whole number: '))
        if userGuess > number:
            print('Your guess was too high')
            print('')
            #Keeps track of how many guesses the user took
            guesses += 1
        elif userGuess < number:
            print('Your guess was too low')
            print('')
            guesses += 1
        else:
            print('You guessed correctly.')
            guesses += 1
            print('It took',guesses,'guesses to get the right number')
            
main()
