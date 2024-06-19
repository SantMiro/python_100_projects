################################
# Title: Caesar Cipher         #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This is the code to encode or decode a word given by the user by shifting a number of positions.'''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(word,shift,letters = letters):
    result = str()
    
    for letter in word:
        displacement = letters.index(letter) + shift
        if displacement >= len(letters):
            displacement -= len(letters)
            result += letters[displacement]
        else:
            result += letters[displacement]
    return result

def decode(word,shift,letters = letters):
    result = str()
    
    for letter in word:
        displacement = letters.index(letter) - shift
        if displacement < 0:
            result += letters[displacement + len(letter) - 1]
        else:
            result += letters[displacement]
    return result

end_of_game = False
while end_of_game == False:
    operation = input('Type "encode" or "decode" to start: \n')
    if operation == 'encode':
        word = input('Type your word: \n').lower()
        shift = int(input(f'Type the shift from 0 to {len(letters)}: \n'))
        result = encode(word,shift)
        print(f'Your encoded word is: {result}.\n')
    elif operation == 'decode':
        word = input('Type your word: \n').lower()
        shift = int(input(f'Type the shift from 0 to {len(letters)}: \n'))
        result = decode(word,shift)
        print(f'Your decoded word is: {result}.\n')
    else:
        print('That is not a valid command. Please try again.')
    
    print('Do you want to try a new word?\n')
    check_user = input('Type "yes" if you want to try again and "no" if you want to stop.')
    if check_user == 'no':
        end_of_game = True