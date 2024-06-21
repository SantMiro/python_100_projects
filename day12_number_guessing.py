################################
# Title: Number Guessing       #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This code generates a random number and the user has to guess which number is it.'''

import random

def guess_number(number):

    '''This function will ask the user for a number to guess until the user loses all lives or the user guesses the correct number.'''
    
    global lives # Set lives to global because it will change depending on the difficulty level
    score = False # Number has not been guessed.
    while lives > 0 and score == False:
        guess = int(input('Guess a number: '))
        lives -= 1 # Every try loses one life.

        if guess > number: # If guess is higher than number.
            if lives == 0:
                print(f'Too high. You have {lives} lives left. You lose!')
                print(f'The correct number was {number}.')
            else:
                print(f'Too high. You have {lives} lives left.')

        elif guess < number: # If guess is lower than number.
            if lives == 0:
                print(f'Too low. You have {lives} lives left. You lose!')
                print(f'The correct number was {number}.')
            else:
                print(f'Too low. You have {lives} lives left.')
        else:
            score = True # If the number is guessed.
            print('You win.')

def number_guessing_game():

    '''Number guessing game app.'''

    keep_plying = input('Do you want to play guess the number? Type "y" for yes or "n" for no. ')

    if keep_plying == 'y': # If user wants to play, select number, and set difficulty.
        number = random.randint(1,100)
        global lives
        difficulty = input('Choose a difficulty level. Type "easy" or "hard".\n')

        if difficulty == 'easy':
            lives = 10 # 10 lives for easy,
            guess_number(number)
        elif difficulty == 'hard':
            lives = 5 # 5 lives for hard.
            guess_number(number)
        number_guessing_game()

number_guessing_game()



    
    
    