################################
# Title: Silent Auction        #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This is the code to perform a silent auction.'''

import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')

def find_highest_bidder(bids):
    max_bid = 0

    for key in bids:
        if bids[key] > max_bid:
            max_bid = bids[key]
            max_bidder = key
    print(f'The highest bidder was {max_bidder} with ${max_bid}!\n')


bids = {}
stop_bidding = False
while not stop_bidding:

    name = input('What is your name? \n')
    bid = int(input('What is your bid? \n'))

    bids[name] = bid
    next_bid = input('Do you want to keep on bidding? Type "yes" or "no". \n')
    
    if next_bid == 'no':
        stop_bidding = True
        clear_screen()
        find_highest_bidder(bids)
    else:
         clear_screen()




          