###################################
# Title: NATO phonetic alphabet   #
# Author: Santiago Miro           #
#       June 2024                 #
###################################


'''This code provides a list of the NATO alphabet depending on the provided name. "exit" finishes program. '''

import pandas as pd

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index,row) in alphabet.iterrows()}

def nato_phonetic():
    name = input('What is your name? ').upper()

    if name == 'exit':
        print('Come back soon!')
    else:
        try:

            nato_letters = [alphabet_dict[letter] for letter in name]

        except KeyError:
            print('Only alphabetical characters supported.')
        else:
            print(nato_letters)
        nato_phonetic()

nato_phonetic()

