#CTI-110
#M6T2 - Feet to Inches Converter
#Aaron Williams
#11/14/2017
#This programs converts feet to inches.

#Constant used to convert feet to inches.
INCH_CONVERTER = 12

def main():
    #Asks user for a distance in feet.
    feet = float(input('Please enter a distance in feet: '))

    conversion(feet)


def conversion(feet):
    #Calculation to convert feet to inches.
    inches = INCH_CONVERTER * feet
    #Displays results.
    print('\nYour distance in feet was:',format(feet,',.2f'),'feet\n'
          'Your distance in inches was:',format(inches,',.2f'),'inches')

main()
