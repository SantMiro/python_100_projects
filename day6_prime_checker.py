################################
# Title: Prime Number Checker  #
# Author: Santiago Miro        #
#        June 2024             #
################################

'''This code calculates if an integer is a prime number or not.'''

def prime_checker(number):
  prime = True #Variable to determine if number is prime.
  for i in range(2,number):
    divs = number % i #Divide each number from 2 to the number itself
    if divs == 0: #If the module is 0, then it is a prime number
        prime = False
        break
  if prime == True:
    print("It\'s a prime number.")
  else:
    print("It\'s not a prime number.")

number = int(input('Type a number to check is it is a prime number: '))

prime_checker(number)
          