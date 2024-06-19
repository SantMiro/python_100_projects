###########################
## Treasure Island       ##
## AUTHOR: Santiago Miro ##
## June 2024             ##
###########################

'''This code resembles a simple prompt game of trasure hunt.'''

print("Welcome, traveler! Find the treasure or die! \n ")
first = input("You are just getting off your ship, you can go either left or right.\n")

if first =='left' or first == 'Left':
    print("You fell off a cliff and you died.")
else:
    print("You found a cave. \n")
    second = input("If you want to go around it type 'around', if you want to enter type 'enter'.\n")
    
    if second == 'around':
        print("There was a bear lurking outside. You died.")
    else:
        print('The treasure was there. You win!')

