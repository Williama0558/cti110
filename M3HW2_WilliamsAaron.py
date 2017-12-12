#CTI-110
#M3HW2 - Software Sales
#Aaron Williams
#10/03/2017
#This program determines how much of a discount will be applied to bulk purchases.

def main():
    #Defines the various discount tiers and sets the price of the software.
    SOFTWARECOST = 99
    tier1Discount = 10
    tier2Discount = 20
    tier3Discount = 50
    tier4Discount = 100
    softwareBought = int(input('Please enter in the amount of copies you are buying: '))

    print('')
    
    #Determines what discount to give the user based on how many copies they bought.
    if softwareBought >= tier4Discount:
        discount4Multiplication = SOFTWARECOST * softwareBought
        discount4Percent = discount4Multiplication * .40
        discount4Total = discount4Multiplication - discount4Percent
        print('You purchased', softwareBought,'copies of software.')
        print('A 40% discount is applied to purchases of 100 or more copies.')
        print('The cost of one copy of the software is $99')
        print('Your discount will be: $',format(discount4Percent,',.2f'))
        print('Before the discount the cost would have been: $',discount4Multiplication)
        print('The total cost of your purchase is: $',format(discount4Total,',.2f'))
    elif softwareBought >= tier3Discount:
        discount3Multiplication = SOFTWARECOST * softwareBought
        discount3Percent = discount3Multiplication * .30
        discount3Total = discount3Multiplication - discount3Percent
        print('You purchased', softwareBought,'copies of software.')
        print('A 30% discount is applied to purchases of 50 or more copies.')
        print('The cost of one copy of the software is $99')
        print('Your discount will be: $',format(discount3Percent,',.2f'))
        print('Before the discount the cost would have been: $',discount3Multiplication)
        print('The total cost of your purchase is: $',format(discount3Total,',.2f'))
    elif softwareBought >= tier2Discount:
        discount2Multiplication = SOFTWARECOST * softwareBought
        discount2Percent = discount2Multiplication * .20
        discount2Total = discount2Multiplication - discount2Percent
        print('You purchased', softwareBought,'copies of software.')
        print('A 20% discount is applied to purchases of 20 or more copies.')
        print('The cost of one copy of the software is $99')
        print('Your discount will be: $',format(discount2Percent,',.2f'))
        print('Before the discount the cost would have been: $',discount2Multiplication)
        print('The total cost of your purchase is: $',format(discount2Total,',.2f'))
    elif softwareBought >= tier1Discount:
        discount1Multiplication = SOFTWARECOST * softwareBought
        discount1Percent = discount1Multiplication * .10
        discount1Total = discount1Multiplication - discount1Percent
        print('You purchased', softwareBought,'copies of software.')
        print('A 10% discount is applied to purchases of 10 or more copies.')
        print('The cost of one copy of the software is $99')
        print('Your discount will be: $',format(discount1Percent,',.2f'))
        print('Before the discount the cost would have been: $',discount1Multiplication)
        print('The total cost of your purchase is: $',format(discount1Total,',.2f'))
    else:
        noDiscount = SOFTWARECOST * softwareBought
        print('You purchased', softwareBought,'copies of software.')
        print('No discount is applied to purchases under 10 copies.')
        print('The cost of one copy of the software is $99')
        print('The total cost of your purchase is: $',format(noDiscount,',.2f'))

main()
