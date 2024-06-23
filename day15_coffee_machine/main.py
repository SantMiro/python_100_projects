################################
# Title: Coffee Machine        #
# Author: Santiago Miro        #
#        June 2024             #
################################

'''This code simulates the software needed for a coffee machine. Where user selects type of coffee and pays with coins.'''

import coffee_recipes # Dictionaries with coffee recipes, the MENU of the coffee machine and the max resources available for each ingredient.

def report(resources): 

    '''Prints the available resources of each ingredient.'''

    print('\nThe current resources available are: \n')
    for ingredient in resources:
        print(f'{ingredient}: {resources[ingredient]}ml.')

def check_resources(MENU,selection,resources):

    '''Checks if the current resources are enough for the selected option.'''

    enough_resources = True
    for ingredient in MENU[selection]['ingredients']:
        if resources[ingredient] < MENU[selection]['ingredients'][ingredient]:
           enough_resources = False
           print(f'Not enough {ingredient}. Try another type of coffee or stock machine.\n')
    return enough_resources

def process_coins(coins):

    '''Asks user for coins. Function counts how many of each value are inserted and calculates total paid.'''

    print('Insert coins:')
    penny = int(input('How many pennies? '))
    nickel = int(input('How many nickel? '))
    dime = int(input('How many dime? '))
    quarter = int(input('How many quarters? '))
    total_paid = (coins['penny'] * penny) + (coins['nickel'] * nickel) + (coins['dime'] * dime) + (coins['quarter'] * quarter)
    print(f'Inserted amount: ${round(total_paid)}.\n')
    return total_paid

def process_payment(total_paid,cost):

    '''Checks if the amount paid by the user is enough to cover the cost of the coffee.'''

    if total_paid < cost:
        enough_coins = False
        print('Not enough funds. Take your money back and try again.\n')
    else:
        enough_coins = True
    return enough_coins

def make_coffee(MENU,selection,resources,total_paid,cost):

    '''This function updates the resources available after making the coffee and returns change to user if needed.'''

    for ingredient in MENU[selection]['ingredients']:
        resources[ingredient] -= MENU[selection]['ingredients'][ingredient]
    if total_paid == cost:               
        print('Please take your coffee.\n')
    else:
        change = round(total_paid - cost,3)
        print(f'Here is your change: ${change}.\n')
        print('Please take your coffee.')
    return resources

def empty_resources(MENU,resources):

    '''If resources are not available for any option this function lets the user know.'''

    any_coffee = {coffee:True for coffee in MENU}
    for coffee in MENU:
        for ingredient in MENU[coffee]['ingredients']:
            if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]:
                any_coffee[coffee] = False
    if not True in any_coffee.values():
        print('No more resources available for any option. Restock machine.\n')

def coffee_machine(resources, MENU, coins):
    
    '''Coffee machine function asks for user selection.'''

    selection = input('Selec the type of coffe you want. (espresso, latte, cappuccino) Type "cancel" to exit.: ')

    if selection == 'cancel' or selection == 'exit':
        print('Have a nice day.')
    elif selection == 'report':
        report(resources=resources)
        coffee_machine(resources=resources, MENU=MENU, coins=coins)
    elif selection in MENU.keys():
        enough_resources = check_resources(MENU=MENU,selection=selection,resources=resources)
        if enough_resources == True:
            cost = MENU[selection]['cost']
            print(f'\nYour total is: ${cost}.\n')
            total_paid = process_coins(coins=coins)
            enough_coins = process_payment(total_paid=total_paid,cost=cost)
            if enough_coins == True:
                resources = make_coffee(MENU=MENU,selection=selection,resources=resources,total_paid=total_paid,cost=cost)
        else:
            empty_resources(MENU,resources)
            
        coffee_machine(resources=resources, MENU=MENU, coins=coins)
    else:
        print('Command not known. Please try again or try a different command\n')
        coffee_machine(resources=resources, MENU=MENU, coins=coins)

resources = coffee_recipes.resources # Resources available in the machine.
MENU = coffee_recipes.MENU # Coffee options in the machine.
coins = coffee_recipes.coins # Coins accepted by machine.

coffee_machine(resources=resources, MENU=MENU, coins=coins)


