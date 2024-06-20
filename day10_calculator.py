################################
# Title: Calculator            #
# Author: Santiago Miro        #
#        June 2024             #
################################

''' This is the code calculates and returns basic arithmetic operations given two numbersS.'''

def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {'+':add,
              '-':substract,
              '*':multiply,
              '/':divide}
def calculator():
    end_running = False
    n1 = float(input('What is the first number? '))
    while not end_running:

        
        print('Choose an operation: \n')
        for symbol in operations:
            print(symbol)
        symbol = input()
        n2 = float(input('What is the second number? '))

        ans = operations[symbol](n1,n2)

        print(f'{n1} {symbol} {n2} = {ans}')

        check = input('Type "y" to continue on the previous result or "n" to start over. ')

        if check == 'n':
            end_running = True
            calculator()
        else:
            n1 = ans
            
calculator()

    