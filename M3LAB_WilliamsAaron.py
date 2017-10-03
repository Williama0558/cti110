#CTI-110
#M3LAB - Debugging
#Aaron Williams
#09/26/2017
#This program was an exercise in trying to debug a faulty grading program.

def methodElif():
    #This method takes a number grade and outputs a letter grade using elif statements.

    #system uses 10-point grading scale
    gradeA = 89.5
    gradeB = 79.5
    gradeC = 69.5
    gradeD = 59.5
    gradeF = 0

    #Section where user inputs their number grade.
    score = float(input('Please enter in your numeric grade: '))

    #Displays the user's letter grade based on the number they entered.
    if score > 100:
        print(score,'is not a valid grade, the scale only goes from 0 to 100')
    elif score >= gradeA:
        print('Your letter grade is an: A')
    elif score >= gradeB:
        print('Your letter grade is a: B')
    elif score >= gradeC:
        print('Your letter grade is a: C')
    elif score >= gradeD:
        print('Your letter grade is a: D')
    elif score >= gradeF:
        print('Your letter grade is an: F')
    else: 
        print(score,'is not a valid grade, the scale only goes from 0 to 100')

def methodNested():
    #This method takes a number grade and outputs a letter grade using nested statements.

    #system uses 10-point grading scale
    gradeA = 89.5
    gradeB = 79.5
    gradeC = 69.5
    gradeD = 59.5
    gradeF = 0

    #Section where user inputs their number grade.
    score = float(input('Please enter in your numeric grade: '))

    #Displays the user's letter grade based on the number they entered.
    if score > 100:
        print(score,'is not a valid grade, the scale only goes from 0 to 100')
    else:
        if score >= gradeA:
            print('Your letter grade is an: A')
        else:
            if score >= gradeB:
                print('Your letter grade is a: B')
            else:
                if score >= gradeC:
                    print('Your letter grade is a: C')
                else:
                    if score >= gradeD:
                        print('Your letter grade is a: D')
                    else:
                        if score >= gradeF:
                            print('Your letter grade is an: F')
                        else:
                             if score < 0:
                                print(score,'is not a valid grade, the scale only goes from 0 to 100')


#program start
methodElif()
methodNested()
