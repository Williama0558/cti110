#CTI-110
#M6T1 - Kilometer Converter
#Aaron Williams
#11/14/2017
#This programs converts kilometers to miles.

#Number used to convert kilometers to miles
CONVERSION = 0.621371

def main():
    #Asks user for a distance in kilometers
    kilometers = float(input('Please enter a distance in kilometers: '))

    mileConverter(kilometers)


def mileConverter(kilometers):
    #Calculation that converts kilometers to miles
    miles = CONVERSION * kilometers
    #Displays results
    print('\nYour distance in kilometers was:',format(kilometers,',.2f'),'kilometers\n'
          'Your distance in miles was:',format(miles,',.2f'),'miles')
    
main()
