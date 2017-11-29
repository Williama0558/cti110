#CTI-110
#M6HW1 - Test Grading
#Aaron Williams
#11/29/17
#This program shows the user the letter grade for each numeric grade they enter
#and then displays the average of all grades entered.

def main():
    numberOfGrades = int(input('How many grades for tests are you entering? '))
    calcAverage(numberOfGrades)


def determineGrade(score):
    #This method takes a number grade and outputs a letter grade using elif statements.

    #system uses 10-point grading scale
    gradeA = 89.5
    gradeB = 79.5
    gradeC = 69.5
    gradeD = 59.5
    gradeF = 0
    
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

def calcAverage(numberOfGrades):
    totalOfGrades = 0
    gradesGraded = 1
    #Will run the loop until the user enter in all the grades they wanted.
    while gradesGraded <= numberOfGrades:
        #User enters the score they got on a test
        score = float(input('What grade did you get on the test? '))
        #Adds the user's score to the totalOfGrades variable
        totalOfGrades += score
        #Increases the variable by one increment
        gradesGraded += 1
        determineGrade(score)
        print('')
    #Finds the average of the grades the user entered
    averageOfGrades = totalOfGrades / numberOfGrades
    print('The average of your grades was:',format(averageOfGrades,',.2f'))

main()
    
