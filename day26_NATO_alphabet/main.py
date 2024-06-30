###################################
# Title: NATO phonetic alphabet   #
# Author: Santiago Miro           #
#       June 2024                 #
###################################


'''This code provides a list of the NATO alphabet depending on the provided name. "exit" finishes program. '''

import pandas as pd

def nato_phonetic():
    name = input('What is your name? ')

    if name == 'exit':
        print('Come back soon!')
    else:
        alphabet = pd.read_csv('day26_NATO_alphabet/nato_phonetic_alphabet.csv')

        nato_letters = [next((row.code for (_,row) in alphabet.iterrows() if row.letter == letter.upper()), None) for letter in name]

        print(nato_letters)

        nato_phonetic()

nato_phonetic()

