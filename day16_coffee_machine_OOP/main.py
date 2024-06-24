#################################
# Title: Coffe Machine with OOP #
# Author: Santiago Miro         #
#        June 2024              #
#################################

'''This file contains the simulation of a coffee machine software, but it is mostly based on OOP as an educational exercise.'''

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Build objects
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Turn on machine
machine_on = True

def coffe_machine(machine_on):
    if machine_on:
        options = menu.get_items() # Get drinks available
        selection = input(f'Select a coffee type: {options} ') #Make selection

        if selection == 'report': # Get reports of available resources and money.
            coffee_maker.report()
            money_machine.report()

        elif selection == 'exit' or selection == 'cancel': # Turn off machine
            machine_on = False

        else:
            drink = menu.find_drink(selection) # Find drink selected in menu
            
            if drink:
                can_make = coffee_maker.is_resource_sufficient(drink) # Find if resources are available for preparation.

                if can_make:
                    print(f'The cost of your drink is: ${drink.cost}') 
                    payment = money_machine.make_payment(drink.cost) # Begin payment process
                    
                    if payment:
                        coffee_maker.make_coffee(drink) # If payment successful then make coffee and update resources.
        coffe_machine(machine_on)

coffe_machine(machine_on)





