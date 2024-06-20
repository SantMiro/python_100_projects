################################
# Title: Blackjack game        #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This code plays a blackjack game against the pc.'''

import random
import time
cards = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

def draw_card():

    '''Randomly chooses a card from the list. Saves its value and symbol.'''
    face = random.choice(card_faces)
    value = cards[face]
    return face, value

def initial_setup():

    ''' In order to start the game, the same process is always repeated. Draw two cards for the player and one for the dealer.
    Sum the value of the drawn cards.'''

    first_draw_face, first_draw_value = draw_card()
    second_draw_face, second_draw_value = draw_card()

    dealer_draw_face, dealer_draw_value = draw_card()

    total = first_draw_value + second_draw_value
    draws = [first_draw_face, second_draw_face]
    dealer_draws = [dealer_draw_face]
    print(f'\nYour starting hand is {draws} = {total}\n')

    print(f'The dealers hand is {dealer_draws} = {dealer_draw_value}\n')

    return draws, dealer_draws, dealer_draw_value, total

def player_turn(draws, total):

    '''When the game starts per turn a card is drawn and then added to the total score. Tha ace can have values of '1' and '11',
    so a condition is implemented.'''

    draw_face, draw_value = draw_card()
    draws.append(draw_face)
    total += draw_value
    if total > 21 and 'A' in draws:
        while total > 21 and 'A' in draws:
            total -= 10
            draws.remove('A')  # Consider one 'A' as 1 instead of 11
            draws.append('A1')
    print(f'\nThe current hand is {draws} = {total}\n')
    return draws, total


card_faces = list(cards.keys())

def blackjack_game():
    
    new_game = input('Type "y" to start a new game of blackjack. Type "n" to cancel.')
    if new_game == 'y':
        draws, dealer_draws, dealer_draw_value, total = initial_setup() # Saves lists of draws and total scores.

        if total < 21:
            blackjack = False
            hit_or_stay = input('Type "y" to get another card or "n" if you want to stay. ') # Draw an extra card or stay.
            stay = False

            if hit_or_stay == 'y':
                while not stay:
                    draws, total = player_turn(draws,total)
                    if total <= 21:
                        hit_or_stay = input('Type "y" to get another card or "n" if you want to stay. ')
                        if hit_or_stay == 'n':
                            stay = True
                    elif total > 21:
                        print('\nYou are over 21!\n')
                        stay = True
        else:
            print('It is BLACKJACK!') # If initial hand is 21, then it is blackjack!
            blackjack = True
         
        time.sleep(1)        
        print('-----------------------------------------------------------------------------------')
        print('\nIt is the dealer\'s turn.\n')

        dealer_draws, dealer_draw_value = player_turn(dealer_draws,dealer_draw_value) # Dealer draws second card.

        lose = False
        win = False
        draw = False
        if dealer_draw_value == 21 and blackjack == True: # Draw if both blackjack.
            draw == True    
        elif dealer_draw_value == 21 and blackjack == False: # Lose if only dealer blackjack.
            lose = True
        elif dealer_draw_value < 21 and blackjack == True: # Win if only player blackjack.
            win = True
        elif dealer_draw_value < 21 and blackjack == False: # If there is no blackjack, the turns are played.
            while dealer_draw_value <= 16:
                time.sleep(1)
                dealer_draws, dealer_draw_value = player_turn(dealer_draws,dealer_draw_value)
                time.sleep(1)
                if dealer_draw_value > 21:
                    print('Dealer busts!')
            if total <= 21 and dealer_draw_value <= 21: # If both under 21, highest score wins.
                if total > dealer_draw_value:
                    win = True
                elif total == dealer_draw_value: # If both scores are the same then it is a draw.
                    draw = True
                elif total < dealer_draw_value:
                    lose = True
            elif total <= 21 and dealer_draw_value > 21: # If only one busts, the other wins.
                win = True
            elif total > 21 and dealer_draw_value <= 21:
                lose = True
            elif total > 21 and dealer_draw_value > 21: # If both bust, then it is a draw.
                draw = True

        if win:
            print('\n                                   You win!\n')
        elif lose:
            print('\n                                   You lose!\n')
        elif draw:
            print('\n                                  It is a draw!\n')
        
        blackjack_game()

blackjack_game()   




    

    


