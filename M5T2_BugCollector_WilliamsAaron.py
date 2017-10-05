#CTI-110
#Bug Collector
#Aaron Williams
#10/05/2017
#This program keeps track of the amount of bugs collected over a period of time.

#This method keeps tracks of bugs collected using for loop statements.
def mainFor():
    total = 0
    
    #Defines how many times the loop will run.
    for day in range(1, 8):
        print('Enter how many bugs were collected for day',day,': ')
        #Section where user inputs how many bugs were collected in a day.
        bugsCollected = int(input())
        #Variable that keeps track of how many bugs have been collected so far.
        total += bugsCollected
    print('You collected',total,'bugs over',day,'days.')



#This method keeps track of bugs collected using while loop statements.
def mainWhile():
    total = 0
    day = 1
    
    #Defines how many times the loop will have to run.
    while day <= 7:
        print('Enter how many bugs were collected for day',day,': ')
        #Section where user inputs how many bugs were collected in a day.
        bugsCollected = int(input())
        #Variable that keeps track of how many bugs have been collected so far.
        total += bugsCollected
        #Advances the day in the loop by one each time it is used.
        day += 1
    #Makes sure that the day displayed at the end of the loop is correct.
    day -= 1
    print('You collected',total,'bugs over',day,'days')

mainWhile()
mainFor()
