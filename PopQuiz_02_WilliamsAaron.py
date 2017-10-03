#CTI-110
#Pop Quiz 02
#Aaron Williams
#10/03/2017
#This program displays a message based on the temperature the user types in.

def main():
    #Section where user inputs the temperature
     temperature = float(input('Please enter in the temperature: '))
     
     #Section that determines what message displays based on the temperature the user typed in.
     if temperature < 40:
            print('A little cold isn\'t it?')
     else:
            print('Nice weather we\'re having')

main()
print('')
main()
print('')
main()
