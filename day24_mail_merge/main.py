#################################
## Send birthday invitations   ##
## AUTHOR: Santiago Miro       ##
## June 2024                   ##
#################################



with(open('./Input/Letters/starting_letter.txt') as f):
    letter = f.read()

with(open('./Input/Names/invited_names.txt') as f):
    names = f.readlines()


for name in names:
    name = name.strip('\n')
    new_letter = letter.replace('[name]',name)
    with open(f'./Output/ReadyToSend/letter_to_{name}.','w') as f:
        f.write(new_letter)
    