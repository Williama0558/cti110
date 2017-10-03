#CTI-110
#M3HW1_AgeClassifier_WilliamsAaron
#Aaron Williams
#09/28/2017
#This program tells the user what their age classification is based on the number they enter

def main():
    #The age classifications.
    infant = 1
    child = 12
    teenager = 19
    adult = 20

    userAge = int(input('Please enter in your age: '))

    #Determines what age class the user is based on the age they entered.
    if userAge <= infant:
        print('Since you are',userAge,'years old, you are an infant.')
    elif userAge <= child:
        print('Since you are',userAge,'years old, you are a child.')
    elif userAge <= teenager:
        print('Since you are',userAge,'years old, you are a teenager.')
    else:
        print('Since you are',userAge,'years old, you are an adult.')
    

main()
