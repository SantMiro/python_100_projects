###########################
## Rock, Paper, Scissors ##
## AUTHOR: Santiago Miro ##
## June 2024             ##
###########################

'''This is a rock, paper, scissors game were the user selects one of the three options and the computer randomly generates a response.'''

## ASCII art for options.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
## End of ASCII art

import random
choices_str = ['Rock','Paper','Scissors']
choices = [rock, paper, scissors]

user_choice = int(input('Type 1 for Rock, 2 for paper and 3 for scissors: ')) - 1 # Get index of selected option from user

print(f"You selected: {choices[user_choice]} \n") #Print selection

pc_choice = random.randint(0,2) # Randomly generate pc selection

print(f'The computer selected: {choices[pc_choice]}') # Print art of selection

if user_choice == pc_choice: # Determine if you win or lose. Given ordinary rock, paper, scissors rules.
    print('You tied!')
elif user_choice > pc_choice and abs(user_choice-pc_choice) == 1:
    print(f"{choices_str[user_choice]} beats {choices_str[pc_choice]}. You win!")
elif user_choice < pc_choice and abs(user_choice-pc_choice) == 1:
    print(f"{choices_str[pc_choice]} beats {choices_str[user_choice]}. You lose!")
elif abs(user_choice-pc_choice) == 2 and user_choice > pc_choice:
    print(f"{choices_str[pc_choice]} beats {choices_str[user_choice]}. You lose!")
else:
    print(f"{choices_str[user_choice]} beats {choices_str[pc_choice]}. You win!")    








