#CTI-110
#M2HW2 - Tip, Tax, and Total
#Aaron Williams
#09/14/2017
#This program calculates the total cost of a meal purchased at a restaurant.

#The constants for this program.
TIP_PERCENT = 0.18
SALES_TAX = 0.07

#Place where the user inputs the cost of their meal before tax and tip.
foodCost = float(input('Please enter the original cost of your food: '))

#Line break.
print('')

#The calculations needed for the program.
tipAmount = TIP_PERCENT * foodCost
salesTaxAmount = SALES_TAX * foodCost
totalCost = foodCost + tipAmount + salesTaxAmount

#Displays the results of the calculations.
print('The original price of your meal was: $', format(foodCost, ',.2f'))
print('At 18%. the amount you should tip for this meal is: $', format(tipAmount, ',.2f'))
print('At 7%, the sales tax for this meal will be: $', format(salesTaxAmount, ',.2f'))
print('The total price of your meal is: $', format(totalCost, ',.2f'))
