###############################
## Random Password Generator ##
## AUTHOR: Santiago Miro     ##
## June 2024                 ##
###############################

'''This code randomly generates a password given the number of letters, symbols and numbers the user specifies.'''

import random

print('Welcome to the password generator!')
n_letters = int(input('How many letters would you like in your password? ')) # Number of letters
n_symbols = int(input("How many symbols do you want in your password? ")) # Number of symbols
n_numbers = int(input("How many numbers do you want in your password? ")) # Number of numbers

#List of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

char_types = [n_letters,n_symbols,n_numbers] # List of how many characters of each type to randomly select from

pw_elements = [] # Password elements in order

for i in range(len(char_types)): # For every character type...
    for _ in range(char_types[i]): # For the range of each character type
        if i == 0:
            pw_elements.append(random.choice(letters)) # Select letter
        elif i == 1:
            pw_elements.append(random.choice(symbols)) # Select symbol
        else:
            pw_elements.append(random.choice(numbers)) # Select number

password = str() # Password with randomize order

for _ in range(len(pw_elements)): # For each element in password in order
    element = random.choice(pw_elements) # Randomly select element
    pw_elements.remove(element) # Remove element from original list
    password += element # Add element to final password

print(f"\n Your password is: \n \n {password} \n")




