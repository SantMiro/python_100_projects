################################
# Title: Caesar Cipher         #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This is the code to encode or decode a word given by the user by shifting a number of positions.'''

#List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_encoder(word,shift,direction,letters=letters):
    result = str()
    if direction == 'decode':
        shift *= -1
    for letter in word:
        if letter in letters:
            displacement = letters.index(letter) + shift
            result += letters[displacement]
        else:
            result += letter
    return result
    
end_of_game = False # Set variable to end the app
while end_of_game == False: 
    direction = input('Type "encode" or "decode" to start: \n') #Ask user if they want to encode or decode.

    word = input('Type your word: \n').lower()
    shift = int(input('Type the shift number: \n'))
    shift = shift % 26
    result = caesar_encoder(word,shift,direction)
    print(f"Your {direction}d word is: {result}.\n")
    
    print('Do you want to try a new word?\n')
    check_user = input('Type "yes" if you want to try again and "no" if you want to stop.') 
    if check_user == 'no':
        end_of_game = True