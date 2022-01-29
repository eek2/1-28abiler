'''
The goal of this project is to take in 3 points
and return the center point and radius for a circle
that intersects all 3 points
'''

'''
This function calculates the distance between two points
'''
def distance (point1, point2):
    ###CODE HERE
    return 0

'''
This function calculates the midpoint between two points
'''
def midpoint (point1, point2):
    ###CODE HERE
    return 0

'''
This function calculates the slope of a line that
intersects between two points
'''
def slope (point1, point2):
    ###CODE HERE
    return 0

'''
This function calculates the slope of a perpendicular line given a slope
'''
def perp (slope):
    ###CODE HERE
    return 0

'''
This function calculates the intersection point between two lines
'''
def intersect (point1, slope1, point2, slope2):
    ###CODE HERE
    return 0

###Helper function do not modify
def parsePoint(inputStr):
    if len(inputStr) == 0:
        raise ValueError("No points were given")
    
    inputStr = inputStr.replace(" ", "")
    commaIndex = inputStr.find(",")
    print(commaIndex, len(inputStr))
    try:
        xVal = float(inputStr[0: commaIndex])
    except ValueError:
        raise ValueError("invalid x point")
    if commaIndex == -1:
        raise ValueError("second point ungiven")
    
    try:
        yVal= float(inputStr[commaIndex+1 : len(inputStr)])
    except ValueError:
        raise ValueError("invalid y point")
    
    return [xVal, yVal]

### Make true if points are desired
getPoints = False

if getPoints:
    p1 = parsePoint(input("Enter point 1: "))

    p2 = parsePoint(input("Enter point 2: "))

    p3 = parsePoint(input("Enter point 3: "))
