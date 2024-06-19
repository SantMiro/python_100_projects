################################
# Title: Hangman Game          #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This is the code to play a hangman game against the computer.'''

import random
import ascii_art as aa
import hangman_words as hw

print(aa.logo)

word_list = hw.word_list
lives = 6
word = random.choice(word_list)

prediction = ['_ ' for _ in range(len(word))]

#print(f'The chosen word was {word}\n')

print('\n',f"{' '.join(prediction)}",'\n')

end_of_game = False

used_letters = []

while not end_of_game:
    guess = input('Choose a letter: ').lower()
    
    if guess in used_letters:
        #used_letters.append(guess)
        print(f'You have already tried this letter: {guess}\n')
    else:
        for index in range(len(word)):
            if word[index] == guess:
                prediction[index] = guess
        
        print('\n',f"{' '.join(prediction)}",'\n')

        if guess not in word:
            print(f'The letter {guess} is not in the word. You lose one live.')
            lives -=1
            if lives == 0:
                end_of_game = True
                print('You lose.')

        if '_ ' not in prediction:
            end_of_game = True
            print('You Win!!\n')
        
        used_letters.append(guess)
        print(aa.stages[lives])
    
    
    
    

