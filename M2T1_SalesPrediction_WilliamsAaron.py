#CTI-110
#M2T1 - Sales Prediction
#Aaron Williams
#09/12/2017
#This program calculates the profit of sales at 23%

#Stores the sales amount that the user inputs.
total_sales = float(input('Please enter the projected sales amount: '))
#Calculates what 23% of the amount you entered will be.
profit = total_sales * 0.23
#Will display what your profit amount is.
print('Your profit is $', format(profit, ',.2f'))
