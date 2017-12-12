#CTI-110
#M2HW1 - Distance Traveled
#Aaron Williams
#09/14/2017
#This program calculates how much distance will be covered going 70 miles per hour at various times.

print('Assuming you are driving 70 miles per hour with no interruptions, you will have:')

#The variables used to calculate distance traveled after various times.
SPEED = 70
distanceAfter6 = SPEED * 6
distanceAfter10 = SPEED * 10
distanceAfter15 = SPEED * 15

#Shows the results of the calculations.
print('driven',distanceAfter6,'miles after six hours.')
print('driven',distanceAfter10,'miles after ten hours.')
print('driven',distanceAfter15,'miles after fifteen hours.')

#Extra stuff not part of original assignment below this comment.
#Line break.
print(" ")

#Place where user inputs their custom time.
customTime = float(input('If you would like to know the result for a different time, please enter it in: '))

#Calculates distance traveled with the inputted time.
distanceCustom = customTime * SPEED

#Displays the result of the inputted time.
print('You will have driven',distanceCustom,'miles after',customTime,' hours have passed')

