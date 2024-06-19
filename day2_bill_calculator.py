###########################
## Bill calculator       ##
## AUTHOR: Santiago Miro ##
## June 2024             ##
###########################

'''This code calculates the amount per person for a bill depending on the tip percentage and number of people involved.'''

total = int(input("What is your total? "))
tip = int(input("How much do you want to tip? 10 15 18 "))
people = int(input("How many people involved? "))

print(f"Your total per person is ${round(total*(1+tip/100)/people,2)}")


