from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

def coffe_machine(machine_on):
    if machine_on:
        options = menu.get_items()
        selection = input(f'Select a coffee type: {options} ')

        if selection == 'report':
            coffee_maker.report()
            money_machine.report()

        elif selection == 'exit' or selection == 'cancel':
            machine_on = False

        else:
            drink = menu.find_drink(selection)
            
            if drink:
                can_make = coffee_maker.is_resource_sufficient(drink)

                if can_make:
                    print(f'The cost of your drink is: ${drink.cost}')
                    payment = money_machine.make_payment(drink.cost)
                    
                    if payment:
                        coffee_maker.make_coffee(drink)
        coffe_machine(machine_on)

coffe_machine(machine_on)





