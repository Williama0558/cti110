#CTI-110
#M3T1 - Areas of Rectangles
#Aaron Williams
#09/21/2017
#This program will calculate the area of two rectangles and tell the user which one is larger.

#Section where the user inputs information for the first rectangle.
firstRectangleLength = int(input('Please enter the length of the first rectangle: '))
firstRectangleWidth = int(input('Please enter the width of the first rectangle: '))

firstRectangleArea = firstRectangleWidth * firstRectangleLength

#Line break.
print('')

#Section where the user inputs information for the second rectangle.
secondRectangleLength = int(input('Please enter the length of the second rectangle: '))
secondRectangleWidth = int(input('Please enter the width of the second rectangle: '))

secondRectangleArea = secondRectangleLength * secondRectangleWidth

#Line break.
print('')

#Section that determines what message will be displayed based on previously entered info.
if firstRectangleArea > secondRectangleArea:
    print('With an area of',firstRectangleArea,', the first rectangle has a larger area than \n'
          'the second rectangle\'s area of',secondRectangleArea)

else:
    if firstRectangleArea < secondRectangleArea:
        print('With an area of',secondRectangleArea,', the second rectangle has a larger area than \n'
          'the first rectangle\'s area of',firstRectangleArea)
        
    elif firstRectangleArea == secondRectangleArea:
        print('The rectangles are equal since they both have an area of:',firstRectangleArea)
